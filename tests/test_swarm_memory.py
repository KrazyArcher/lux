import unittest
import time
from swarm_memory import SwarmMemory

class TestSwarmMemory(unittest.TestCase):
    def setUp(self):
        self.sm = SwarmMemory()

    def test_write_and_read(self):
        self.sm.write_agent_state("AGENT_01", {"task": "fetch_bounty"})
        res = self.sm.read_agent_state("AGENT_01")
        self.assertEqual(res["task"], "fetch_bounty")

    def test_ttl_expiry(self):
        # Set TTL to 0 to simulate immediate expiry
        self.sm.write_agent_state("AGENT_02", {"task": "secret_task"}, ttl=0)
        time.sleep(0.1) # Ensure time passes
        res = self.sm.read_agent_state("AGENT_02")
        self.assertIsNone(res)

if __name__ == '__main__':
    unittest.main()
