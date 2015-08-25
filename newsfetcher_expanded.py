

__author__ = 'Nils'

import praw

def main():


    r = praw.Reddit(user_agent='Newsfetcher by /u/vicerunt')
    print("Choose your desired subreddit:")
    # Stores the entered subreddit in userchoice.
    userchoice = input("Your choice: ")
    # Gets 30 top posts from the specific subreddit.
    submissions = r.get_subreddit(userchoice).get_top(limit=30)
    # Formats the printed output and adds a nice counter:
    submission_form = "{}) {} : {} <{}>"
    count = 1
    print("Top 30 Posts from", userchoice)
    print('-' * 25)
    for sub in submissions:
        print(submission_form.format(count, sub.ups, sub.title, sub.url))
        count +=1

if __name__ == "__main__":
    main()