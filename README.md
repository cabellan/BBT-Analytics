# BBT-Analytics

In this repository we show a couple of examples on how to manipulate and process the data that were created during the BIG Bell test project. We use Python, and more specifically, the libraries numpy and pandas. Pandas is a very convienent library for analyzing datasets like the one collected during this project.

The dataset contains a row for every single mission that was played through the website http://thebigbelltest.org. Each row contains both information about the mission and also about the user. Namely, a user that played 10 missions will have 10 rows in the dataset. More specifically, these are the fields in each row:

- username_id (String)    
- gender (String, which can be 'male'/'fem'/'none')
- birth year (Number, e.g. 1990 (default value is 1900)
- instrument? (String, arbitrary input string, e.g. guitar/piano/...)
- timestamp (Number, number of milliseconds since 1 January 1970)
- Bits (String  with all the bits for that missions)
- Mean (Number, average value of the sequence described in Bits)
- Mission (Number, contains the mission number, i.e. 1, 2, 3, 4, 5, 6)


_Filtering data_
The dataset that you can access contains all the information that was created during the project. As such, it contain some missions that you probably will want to discard when analyzing the dataset.  Some examples of filters to apply:
- Timestamp: You might want to start processing data after some specific date (early stage sequences might contain participations during development time, and therefore, not being good samplings of human randomness). Since the timestamp was created in frontend (i.e. in the browser of the users), the value that gets recorded might have been modified by malicious participants. This might be an efficient way to discard data. If the date does not make sense (e.g. not from 2016), you can discard those rows.

- Bots: it might have happened that some players managed to feed bits from an algorithm into the platform. During the experiments, we implemented some real-time analytics to filter those scenarios out, so that those bits didn't make it to the labs. However, we stored everything in database, and you have access to everything. For instance, you will find users that introduced exactly the same bits multiple times, meaning that somehow they copy pasted the bits multiple times. One way to filter those data out might be to first identify players who played a suspiciously large number times and investigate their contributions.

- Non-cooperatives:  You’ll find multiple entries that contain trivial sequences like '11111...' or '00000...' or '1010101...'. Although some of those might in principle be real attempts to behave randomly, most are probably people testing the system, to see _"what happens if I do this?"_. You might want to discard those missions based on the evident non-cooperation with the game instructions.
