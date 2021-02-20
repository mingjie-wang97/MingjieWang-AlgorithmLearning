
"""
Question:
you want to get the best living area block; 
best living block: a block that has the minimum distance comparing with other blocks to reach
	all facilities you list in reqs
distance: maximum distance to reach to all facilities in reqs

giving blocks and reqs
return the index of the block

n: blocks length; m: reqs length
time: O(2 * n + n * m) -> O(n * m)
space: O(n * m)
"""

def find_min_dis(blocks, reqs):
	# edge case; assume length of each block is the same as length of reqs
	if not blocks: return "No Block Existed"
	if not reqs: return 0

	dist = [{item: float("inf") for item in reqs} for _ in range(len(blocks))]
	closest = {item: -1 for item in reqs}

	for i, block in enumerate(blocks):
		for item in block:
			# only execute when block[item] is TRUE
			if block[item]:
				# check the previous closest TRUE item; compare and set max distance
				temp = i
				while temp >= 0 and temp >= closest[item]:
					if closest[item] >= 0:
						temp_i = i - temp
						temp_closest = temp - closest[item]
						dist[temp][item] = min(temp_i, temp_closest)
					else:
						dist[temp][item] = i - temp
					temp -= 1
				closest[item] = i
		# if this block has all reqs, directly return
		s = set(closest.values())
		if len(s) == 1 and -1 not in s: return s.pop()
	
	# final process -> mark all last inf item into distance
	for item in block:
		temp = len(blocks) - 1
		while temp >= 0 and temp >= closest[item]:
			if closest[item] < 0: return "Not Existed"
			else:
				dist[temp][item] = temp - closest[item]
			temp -= 1

	output, output_dist = -1, float("inf")
	for i in range(len(blocks)):
		temp = max(dist[i].values())
		if temp < output_dist:
			output_dist = temp
			output = i
	return output


blocks = [
	{"gym": False, "school": True, "store": False},
	{"gym": True, "school": False, "store": False},
	{"gym": True, "school": True, "store": False},
	{"gym": False, "school": True, "store": False},
	{"gym": False, "school": True, "store": False},
	{"gym": True, "school": True, "store": False}
]
reqs = ["gym", "school", "store"]

print(find_min_dis(blocks, reqs))