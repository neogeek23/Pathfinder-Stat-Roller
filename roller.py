import random
import time


def new_character_roller(primary_stat, secondary_stat, min_pstat, min_stat, max_stat, max_stats_allowed,
						 max_stat_expected, odd_allowed, counter):
	result = [8, 8, 8, 8, 8, 8]
	ps = stat_translator(primary_stat)
	ss = stat_translator(secondary_stat)

	if ps is None or ss is None:
		return None

	# Reroll whole set if any of these things are true:  Primary Stat too low, Secondary Stat too low, Some Stat too low
	# rolls have too many good numbers or not enough good numbers, too many odd numbers
	while result[ps] < min_pstat or result[ss] < (min_pstat - 2) or lowest_roll(result) < min_stat or result[2] < 10 \
			or not is_buff(result, max_stat, max_stats_allowed, max_stat_expected) or odds_allowed(result, odd_allowed):
		for i in range(len(result)):
			result[i] = roll_4d6d11(counter)
		counter[1] += 1
	return result


def roll_4d6d11(counter):
	low = 7
	sum_hold = 0
	for x in range(4):
		roll = random.randint(1, 6)
		sum_hold += roll

		if roll < low:
			low = roll
		counter[0] += 1
	return sum_hold - low


def stat_translator(stat_name):
	if stat_name == 'Str':
		return 0
	elif stat_name == 'Dex':
		return 1
	elif stat_name == 'Con':
		return 2
	elif stat_name == 'Int':
		return 3
	elif stat_name == 'Wis':
		return 4
	elif stat_name == 'Cha':
		return 5
	else:
		print("Unmatched Primary Stat")
		return None


def lowest_roll(rolls):
	low = 20
	for roll in rolls:
		if roll < low:
			low = roll
	return low


def odds_allowed(rolls, odd_tolerance):
	count = 0
	for roll in rolls:
		if roll % 2 == 1:
			count += 1
	# if odd_tolerance >= count:
	# 	print("Character Odd Stat test failed.")
	return odd_tolerance < count


def is_buff(rolls, max_tolerance, max_allowed, max_expected):
	count = 0
	for roll in rolls:
		if roll >= max_tolerance:
			count += 1
	# if max_expected > count or count > max_allowed:
	# 	print("Character Buff test failed.")
	return max_expected <= count <= max_allowed


def party_roller(separation, sum_min, sum_max, stat_priority, a, b, c, d, e, f, counter):
	stat_group = []
	i = 0

	while len(stat_group) < len(stat_priority):
		roll_set = new_character_roller(stat_priority[i][0], stat_priority[i][1], a, b, c, d, e, f, counter)
		if roll_set is None:
			print("New Character Roller returned None, address this error and try again.")
		stat_group.append(roll_set)
		i += 1

		if len(stat_group) == len(stat_priority) and (\
				not group_within_separation(stat_group, separation) or
				not group_set_range(stat_group, sum_max, sum_min) or
				not snowflakes(stat_group, stat_priority)):
			# print("Party Requirements Failed.")
			stat_group = []
			i = 0
			counter[2] += 1
			if counter[2] % 10000 == 0 and not counter[2] % 100000 == 0:
				print("Still working.")
			elif counter[2] % 100000 == 0:
				print("Working harder, working stronger...")
	return stat_group


def group_set_range(stat_set, max_sum, min_sum):
	result = True
	for ss in stat_set:
		sum_hold = 0
		for s in ss:
			sum_hold += s
		result &= min_sum <= sum_hold <= max_sum
	# if not result:
	# 	print("Group Range test failed.")
	return result


def group_within_separation(stat_set, separation):
	lowest = 1000
	biggest = 0

	for ss in stat_set:
		sum_hold = 0
		for s in ss:
			sum_hold += s
		if sum_hold < lowest:
			lowest = sum_hold
		if sum_hold > biggest:
			biggest = sum_hold

	# if biggest-lowest > separation:
	# 	print("Group Separation test failed.")
	return biggest-lowest <= separation


def snowflakes(stat_set, snowflake_set):
	result = True

	for ss in stat_set:
		ss_index = stat_set.index(ss)
		ss_ps = stat_translator(snowflake_set[ss_index][0])

		for s in stat_set:
			s_index = stat_set.index(s)
			s_ps = stat_translator(snowflake_set[s_index][0])
			if s != ss and ss_ps != s_ps:
				result &= s[ss_ps] < ss[ss_ps]
	# if not result:
	# 	print("Snowflake test failed.")
	return result


def taber(stat_set, index):
	longest_string = 0
	result = "\t"

	for ss in stat_set:
		if len(str(ss)) > longest_string:
			longest_string = len(str(ss))

	difference = longest_string - len(str(stat_set[index]))
	extra_tabs = int(difference/4)

	for i in range(extra_tabs):
		result += "\t"
	if difference % 4 > 0:
		result += "\t"
	return result


c = [0, 0, 1]
stat_time = time.time()
# 1) Primary Stat
# 2) Secondary Stat
# 3) Primary Stat Low Value (exclusive)
# 4) Global Low Value (exclusive)
# 5) Global High Value (inclusive)
# 6) Upper Limit (inclusive) of rolls as large or greater than Global High Value
# 7) Lower Limit (inclusive) of rolls at least as large as Global High Value
# 8) Number of odd roles allowed (inclusive)
# 9) How distant sum of each character's stats can be - player balance
# 10) Upper bound for each player stat sum (inclusive bound) - standard fantasy is 15 point buy on top of 10's, so 75
# 11) Lower bound for each player stat sum (inclusive bound)
# See key above      9  10  11 	   1	  2	   1	  2	   1 	  2	   1  	  2  	   3  4   5  6  7  8
stats = party_roller(0, 75, 75, [["Wis", "Str"], ["Cha", "Int"], ["Int", "Wis"], ["Cha", "Dex"]], 14, 7, 16, 2, 1, 3, c)
print("Inquisitor roll is\t" + str(stats[0]) + taber(stats, 0) + "sum:  " + str(sum(s for s in stats[0])))
print("Sorcerer roll is\t" + str(stats[1]) + taber(stats, 1) + "sum:  " + str(sum(s for s in stats[1])))
print("Psychic roll is\t\t" + str(stats[2]) + taber(stats, 2) + "sum:  " + str(sum(s for s in stats[2])))
print("Rouge roll is\t\t" + str(stats[3]) + taber(stats, 3) + "sum:  " + str(sum(s for s in stats[3])))
print("Finding the Magic Rolls took " + str(round((time.time() - stat_time)/60, 3)) + " minutes.")
print(str(c[0]) + " rolls were made for " + str(c[1]) + " characters in " + str(c[2]) + " parties.")
