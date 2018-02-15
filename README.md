# Pathfinder-Stat-Roller
Stat roller for pathfinder

This is a simple stat roller for a party for Pathfinder.  Input (parameters) is added to line 186 of roller.py.  Comments above that line explain the input.  Basically, you can choose your class and then use this to roll random stats for your character with certain assurances.  

Character Parameters:

You can specify a primary and secondary stat for multiple characters and a minimum value for primary stats and secondary stats will have a value of at least primary stat minimum - 2.  You can also set a global minimum value so you can be sure no single stat will be below that value.  You can set a global high value and a maximum and minimum frequency of a value per character.  You can also set a maximum value for the number of odd valued rolls per character.  There is also a snowflake rule in place that a character with a given stat as primary will not have that stat lower than any other character that does not also have that stat as primary.  For example if Character A has Str as primary, he will be guarateed to have greater Str than any character that has a primary stat that is not Str.  These assurances allow characters to have both a functional class preselected and unique rolls to promote organic character growth.  Characters are interpreted as pairs of primary and secondary stat prefrences.

Group Parameters:

You can specify how distant the sum of any player's stats would be to any other player.  This allows for there to be a band placed around balance in base stats.  You can also specify the range of where the sum of the stats should fall.  According to the pathfinder rule book this allows you to control the campaign type (Low, Standard, High, or Epic Fantasy).  Using the point buy system to compare to, base stats start at 10 for a total of 60 + 10, 15, 20, or 25 extra points depending on the campaign type.  For example if a Standard Campaign type is desired, setting the range could be from 74 to 76.

Example Output:

Inquisitor roll is	[15, 16, 10, 7, 16, 12]	  sum:  76
Sorcerer roll is	  [17, 8, 13, 10, 14, 14]	  sum:  76
Psychic roll is		  [12, 12, 15, 16, 8, 13]	  sum:  76
Rouge roll is		    [9, 13, 14, 10, 14, 16]	  sum:  76
Finding the Magic Rolls took 0.947 minutes.
20821392 rolls were made for 867558 characters in 16809 parties.

Inquisitor roll is	[15, 13, 10, 12, 16, 8]	  sum:  74
Sorcerer roll is	  [12, 8, 11, 12, 15, 16] 	sum:  74
Psychic roll is		  [11, 10, 10, 16, 14, 13]  sum:  74
Rouge roll is		    [12, 12, 17, 9, 10, 14]	  sum:  74
Finding the Magic Rolls took 8.008 minutes.
180359088 rolls were made for 7514962 characters in 145234 parties.

Inquisitor roll is	[13, 12, 16, 9, 15, 10] 	sum:  75
Sorcerer roll is	  [16, 8, 16, 8, 12, 15]	  sum:  75
Psychic roll is		  [9, 14, 10, 17, 12, 13] 	sum:  75
Rouge roll is		    [9, 13, 12, 13, 10, 18]	  sum:  75
Finding the Magic Rolls took 23.199 minutes.
517797864 rolls were made for 21574911 characters in 416266 parties.
