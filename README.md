# video-YangHuNU

## Flask API
The following screenshot is a sample output after flask implementation.  
![](./doc/sample.png)

To have the output run on AWS, go to [this address](http://demo2.eba-r47skcmu.us-east-2.elasticbeanstalk.com/)

## Tasks
* Convert text into an image in a frame
* Do a sequence of all texts and images in chronological order
* Display each video frame for 3 seconds

## How to execute
Need to install tweepy and acquire Twitter API key

`pip install tweepy`

Need to install ffmpeg

`pip install ffmpeg`

You will also need to provide your own API tokens and secrets by creating a file named 'keys'. The content of keys should look like:

```
[auth]
consumer_key = ****
consumer_secret = ****
access_token = ****
access_secret = ****
```

To run the code, type in command line

`python main.py`

Then, provide 4 Twitter user IDs.

## Output
For each Twitter user that is entered, 3 tweets from there timeline will be fetched and converted into an image.
All 4 images that have been collected will be made into a output.avi file, which is a video displaying every image for 3 seconds.

What will be out put to the command line window shoud look like the image below.

![CL](./doc/CL_output.png)

## Computer performance
I have a dual-core processor with 2.9GHz. For each core, 4 threads can be run.
Here is a graph generate by [python code for process Vs. thread](https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python)

![Performance](./doc/Performance.png)


## Questions to be Answered
- How many API calls you can handle simultaneously and why?
    + 4 API calls are handled simultaneously. It is a reasonable number that is easy to read and test. For my and most computers, it is an acceptable thread number to process.
- Split API calls at the same time?
    + Yes. Inputs for API calls are collected at once and queued and the queue can be called at the same time.
- Split the processing of an API into multiple threads?
    + For an individual API call, there is no part of it is splitted.

## References
[queue](https://docs.python.org/3/library/queue.html)
[threading](https://docs.python.org/3/library/threading.html)
[python code for process Vs. thread](https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python)
[tweepy](http://docs.tweepy.org/en/latest/)
