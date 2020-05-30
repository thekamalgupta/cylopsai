# cylopsai
A simple virtual assistant program built using Python3

This virtual assistant is able to give speech output and use user speech as input to execute commands. 
The following features are implemented in version 1 of the Cylops Virtaual Assistant:

1. Greeting the user with current date and time upon launch.
2. Search for a query on wikipedia and give out its summary in both text and speech format. (like : "Search for Python on Wikipedia")
3. Send out mails using the assistant by simply asking it "Send an email" or "Send a mail".
4. Open a page in web browser (chrome as of version 1 ).
5. Logout, shutdown or restart your computer system.
6. Play songs from your local library by simply telling Cylops to "Play a song".
7. Cylops can tell you random jokes if you ask for it.
8. Take a screenshot by saying "Screenshot".
9. Get current CPU and battery statistics for your system by saying "current battery/cpu level".
10. Exit the program by saying "Cylops go offline" and it will wish you good day :).

This program uses pttsx3 module for text-to-speech functions and SpeechRecognition module for speech recognition.
The speech recognition is done through Google speech recognition service.
