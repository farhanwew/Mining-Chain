import asyncio
from mining_agents.manager import MiningOperationManager
import os
from dotenv import load_dotenv

load_dotenv()

async def main() -> None:
    """
    Entrypoint for the Mining Value Chain Optimization agent system.
    """
    print("Initializing Mining Operation Manager...")
    mgr = MiningOperationManager()
    await mgr.run()


if __name__ == "__main__":
    # Note: The 'agents' SDK is async-first.
    # We use asyncio.run to start the manager.
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred during execution: {e}")
