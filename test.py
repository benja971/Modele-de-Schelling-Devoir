import os

files = os.listdir('./resultats/Curves/INS_evolution')

l = 15

for file in files:
	if file.endswith('.png'):
		tmp = file.split('_' or '.')
		last = tmp.pop(len(tmp)-1)
		for i in last.split('.'):
			tmp.append(i )

		tmp[len(tmp)-2] = str((15 * 15) - l)
		tmp2 = [tmp.pop(len(tmp)-1) for i in range(2)]
		tmp2.reverse()
		ext = ".".join(tmp2)
		new_name = "_".join(tmp)
		name = new_name + '_' + ext
		os.rename('./resultats/Curves/INS_evolution/' + file, './resultats/Curves/INS_evolution/' + name)
		l += 1