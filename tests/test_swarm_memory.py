import unittest
import time
import sys
import os

# Dynamically injecting parent directory to python path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from swarm_memory import SwarmMemory

class TestSwarmMemory(unittest.TestCase):
    def setUp(self):
        self.sm = SwarmMemory()

    def test_write_and_read(self):
        self.sm.write_agent_state("AGENT_01", {"task": "fetch_bounty"})
        res = self.sm.read_agent_state("AGENT_01")
        self.assertEqual(res["task"], "fetch_bounty")

    def test_ttl_expiry(self):
        self.sm.write_agent_state("AGENT_02", {"task": "secret_task"}, ttl=0)
        time.sleep(0.1)
        res = self.sm.read_agent_state("AGENT_02")
        self.assertIsNone(res)

if __name__ == "__main__":
    unittest.main()
