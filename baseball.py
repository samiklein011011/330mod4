#python, baseball

#imports
import re
import sys, os
import operator


def getStats(fileName):
	with open(fileName) as file:
		totalDictionary={}

		for line in file:
			# print(line)
			if not(re.search('^===', line) or not line.strip() or re.search('^#', line)):
				namePat="^(\w+\s){2}"
				nameMatch = re.search(namePat, line)
				if nameMatch is not None:
					name = nameMatch.group()
					# print(name)

				numsPat='\d'
				numsMatch = re.findall(numsPat, line)
				if numsMatch is not None:
					atBats=int(numsMatch[0])
					hits=int(numsMatch[1])

					if name in totalDictionary:
						tempAtBats=totalDictionary[name][0]
						tempHits=totalDictionary[name][1]
						totalDictionary[name][0] = totalDictionary[name][0] + atBats
						totalDictionary[name][1] = totalDictionary[name][1] + hits

					else:
						totalDictionary[name] = [int(atBats), int(hits)]
						# print(totalDictionary)
						# print(totalDictionary[name][0])


						# totalDictionary[name] = nums


		avgDictionary={}
		for player in totalDictionary:
			# print player

			atBats=float(totalDictionary[player][0])
			hits=float(totalDictionary[player][1])
			# print(atBats)
			# print(hits)
			avg = float(hits/atBats)
			# print avg
			roundedAvg=round(avg,3)
			avgDictionary[player]=roundedAvg




		#SORT NOW
		# got this from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
		sorted_list=sorted(avgDictionary.items(), key=lambda x: x[1], reverse=True)
		for key in sorted_list:
			print "%s: %s" %key






#main method

#usage message
if len(sys.argv) < 2:
	sys.exit("Usage: not enough arguments")

filename = sys.argv[1]

if not os.path.exists(filename):
	sys.exit("Error: File  not found")
    #sys.exit(f"Error: File '{sys.argv[1]}' not found")

#calling function
getStats(filename)
