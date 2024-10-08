from cow import Cow

def get_cows():
	if HeiferGenerator.cows is None:
		HeiferGenerator.cows = [None] * len(HeiferGenerator.cowImages)
		for index in range(len(HeiferGenerator.cows)):
			HeiferGenerator.cows[index] = Cow(HeiferGenerator.cowNames[index])
			HeiferGenerator.cows[index].set_image(HeiferGenerator.quoteLines + HeiferGenerator.cowImages[index])

	return HeiferGenerator.cows


class HeiferGenerator:

	cows = None

	cowNames = ['heifer', 'kitteh']

	quoteLines = '    \\\n' 
	quoteLines += '     \\\n'
	quoteLines += '      \\\n';

	cowImages = [	"        ^__^\n" +
					"        (oo)\\_______\n" +
					"        (__)\\       )\\/\\\n" +
					"            ||----w |\n" +
					"            ||     ||\n",


					"       (\"`-'  '-/\") .___..--' ' \"`-._\n" +
					"         ` *_ *  )    `-.   (      ) .`-.__. `)\n" +
					"         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n" +
					"      _.. `--'_..-_/   /--' _ .' ,4\n" +
					"   ( i l ),-''  ( l i),'  ( ( ! .-'\n",
				]
"""if __name__ == "__main__":
	get_cows()
	print(HeiferGenerator.cows[0].get_image())"""