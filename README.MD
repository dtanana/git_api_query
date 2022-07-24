Greetings, Fair Grader.

So first off, kind of an interesting and good example. Coodos to you Mailchimp Hiring QA Team!

To install my script on MacOS, Which I guess I can say is the recommend place to install, please ensure you are on Python 3.9.12 whatever the platfrom

the next step after you have gone into the folder you unziped this to and to "pip install -r requirements.txt"

If you are MacOS you can the run "chmod +x repo_query.py" to make running this easier. You can now use "./repo_query.py --help" to view the commands option
it takes one arg a github.com/<user>/<repo> url add https:// if you like typing more.

Windows Users you should be able to run " py repo_query.py --help". I think windows and python together
can make a hard life

Full disclosure I did this chunks because there are no 4 hour blocks for things other than sleep and I probably went 30 minutes over the time limit... sorry.

From a perspective of what you wanted
Functionality

Does the code do what it should?
 Yes! I mean at least I think. Release Name is going to be the version but technical that schema also has the Tag as the version both are printed.

Does it handle edge cases?
    Lets jam on that. For what I can catch of common things is user passes github.com/username I deal with that by saying something is wrong
    I catch 400 errors
    I catch 500 but those are hard to create
    I catch instance where repos send a 200 success but less then three resuls
    I would love to know what I am missing but thats the bigest edge cases.

Code quality
    I would like to think its pretty good, python makes that easy and I tried my best to keep it concise while catching said errors.

Is the code readable & maintainable?
    Absolutely in my opinion. I have split the view(ie the cli component) from the controller(request to github)
    which should make this easy to call in a bash for loop

Is there reasonable test coverage?
    Didn't include any, didn't have time and to be quite honest, given the choice in a crunch time script between test coverage/
    error handling. I would prefer to get this out the door with error handling

Performance
    She runs like a dream.

Does the code balance reasonably fast execution with readability?
    I think so but you can let me know
Can the implementation handle large inputs gracefully?
    I mean I think at somepoint if we were going to schale this up I would put in a new line delimited option to chug through a lot of files

Pragmatism
    Thus I ignored unit testing and caught commmon mistakes

Are the above factors balanced well against the limited time to implement the solution?
    I think so

