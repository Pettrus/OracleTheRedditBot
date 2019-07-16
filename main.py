
from image import saveSubmission, saveComment
from reddit import hotQuestions, moreComments
from ffmpeg import createVideo
from tts import get_token, save_audio

def getUserInput(questions):
    print("Type the number corresponding to the Reddit thread(1-8)")

    userInput = input()

    if userInput.isdigit() == False or int(userInput) > 8 or int(userInput) < 1:
        print("Not a valid number")
        getUserInput(questions)
    else:
        start(questions[int(userInput)-1])

def start(submission):
    submission.comment_sort = "best"
    submission.comment_limit = 70

    saveSubmission(submission.title)

    access_token = get_token()
    save_audio(submission.title, "frame1", access_token)

    num = 2

    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, moreComments()):
            continue

        if len(top_level_comment.body) <= 900:
            saveComment(top_level_comment.author.name, top_level_comment.body, 42, num)
            save_audio(top_level_comment.body, "frame" + str(num), access_token)

            print("Frame " + str(num) + " completed")
            num += 1
    
    createVideo(num-1, submission.title)


print("Searching...")

questions = hotQuestions()
qList = []

for num, sub in enumerate(questions, start=1):
    qList.append(sub)
    print(str(num) + " - " + sub.title)

getUserInput(qList)