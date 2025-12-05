import os
from helpers import tsprint, ttime

#data = open(0).read().splitlines()
ranges, ingredients = open(0).read().split("\n\n")
ranges = ranges.splitlines()
ingredients = ingredients.splitlines()

### Solution for part one
def part_one():
  answer = 0
  for ingredient in ingredients:
    for fresh in ranges:
      start, end = map(int, fresh.split("-"))
      if int(ingredient) in range(start, end + 1):
        answer += 1
        break

  tsprint(f"First answer: {str(answer)}")
  return ttime()


### Solution for part two
def part_two():
  answer = 0
  fresh_ids = []
  parsed = []
  for fresh in ranges:
    start, end = map(int, fresh.split("-"))
    parsed.append((start, end))
    parsed.sort()

    combined = []
    cur_start, cur_end = parsed[0]
    for start, end in parsed[1:]:
        if start <= cur_end + 1:  # overlapping or touching
            cur_end = max(cur_end, end)
        else:
            combined.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    combined.append((cur_start, cur_end))

  answer = sum(end - start + 1 for start, end in combined)

  tsprint(f"Second answer: {str(answer)}")
  return ttime()


### Running the solutions
tsprint(f"Starting {os.path.basename(os.getcwd())}")
part_one_time = part_one()
part_two_time = part_two()
tsprint(
  f"Part two took {round(part_two_time / part_one_time, 2)} times longer than part one"
)
tsprint(f"Finished {os.path.basename(os.getcwd())}")
