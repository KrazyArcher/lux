import json
import time

class SwarmMemory:
    def __init__(self):
        self.ledger = {}
        
    def write_agent_state(self, agent_id, context, ttl=3600):
        # Writes state with Time-To-Live (TTL)
        self.ledger[agent_id] = {
            "context": context,
            "expiry": time.time() + ttl
        }
        
    def read_agent_state(self, agent_id):
        # Reads only if TTL has not expired
        state = self.ledger.get(agent_id)
        if not state:
            return None
        if time.time() > state['expiry']:
            del self.ledger[agent_id]
            return None
        return state['context']
