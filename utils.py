import os
import requests
from dotenv import load_dotenv

load_dotenv()

aoc_token = os.getenv('AOC_TOKEN')

def get_puzzle_input(day: int) -> str:
    return requests.get(f"https://adventofcode.com/2025/day/{day}/input", headers={"Cookie": f"session={aoc_token}"}).text