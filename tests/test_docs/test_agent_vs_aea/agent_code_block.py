# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This scripts contains code from agent-vs-aea.md file."""

import os
import time
from threading import Thread
from typing import List, Optional

from aea.agent import Agent
from aea.configurations.base import ConnectionConfig
from aea.connections.base import Connection
from aea.connections.stub.connection import StubConnection
from aea.identity.base import Identity
from aea.mail.base import Envelope
from aea.protocols.default.message import DefaultMessage


INPUT_FILE = "input_file"
OUTPUT_FILE = "output_file"


class MyAgent(Agent):
    def __init__(self, identity: Identity, connections: List[Connection]):
        super().__init__(identity, connections)

    def setup(self):
        pass

    def act(self):
        print("Act called for tick {}".format(self.tick))

    def react(self):
        print("React called for tick {}".format(self.tick))
        while not self.inbox.empty():
            envelope = self.inbox.get_nowait()  # type: Optional[Envelope]
            if (
                envelope is not None
                and envelope.protocol_id == DefaultMessage.protocol_id
            ):
                sender = envelope.sender
                receiver = envelope.to
                envelope.to = sender
                envelope.sender = receiver
                envelope.message = DefaultMessage.serializer.decode(envelope.message)
                print(
                    "Received envelope from {} with protocol_id={}".format(
                        sender, envelope.protocol_id
                    )
                )
                self.outbox.put(envelope)

    def update(self):
        print("Update called for tick {}".format(self.tick))

    def teardown(self):
        pass


def run():
    # Ensure the input and output files do not exist initially
    if os.path.isfile(INPUT_FILE):
        os.remove(INPUT_FILE)
    if os.path.isfile(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    # Create an addresses identity:
    identity = Identity(name="my_agent", address="some_address")

    # Set up the stub connection
    configuration = ConnectionConfig(
        input_file_path=INPUT_FILE,
        output_file_path=OUTPUT_FILE,
        connection_id=StubConnection.connection_id,
    )
    stub_connection = StubConnection(configuration=configuration, identity=identity)

    # Create our Agent
    my_agent = MyAgent(identity, [stub_connection])

    # Set the agent running in a different thread
    try:
        t = Thread(target=my_agent.start)
        t.start()

        # Wait for everything to start up
        time.sleep(3)

        # Create a message inside an envelope and get the stub connection to pass it into the agent
        message_text = (
            b"my_agent,other_agent,fetchai/default:0.3.0,\x08\x01*\x07\n\x05hello,"
        )
        with open(INPUT_FILE, "wb") as f:
            f.write(message_text)

        # Wait for the envelope to get processed
        time.sleep(2)

        # Read the output envelope generated by the agent
        with open(OUTPUT_FILE, "rb") as f:
            print("output message: " + f.readline().decode("utf-8"))
    finally:
        # Shut down the agent
        my_agent.stop()
        t.join()


if __name__ == "__main__":
    run()
