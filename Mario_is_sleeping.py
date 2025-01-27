#Alex Kreimann
#27.01.2025
#Siin on mingi tekst

import requests
import json

inimene=int(input("Palun sisestage ID(1-20): "))
url='https://dummyjson.com/users'
response=requests.get(url)

if response.status_code==200:
    data=response.json()
    for i in data:
        if inimene in ['quote']:
            print(i['quote'])    
else:
    print("Viga andmete allalaadimisel, idikas!:"), response.status_code

{
  "Content-Type": "application/json"
}

[
    {
      "id": 1,
      "quote": "The only way to do great work is to love what you do.",
      "author": "Steve Jobs",
      "authorImage": "https://example.com/steve_jobs.jpg",
      "date": "2005-06-12T15:30:00Z",
      "category": "Motivation",
      "popularityIndex": 95
    },
    {
      "id": 2,
      "quote": "In three words I can sum up everything I've learned about life: it goes on.",
      "author": "Robert Frost",
      "authorImage": "https://example.com/robert_frost.jpg",
      "date": "1956-04-23T12:15:00Z",
      "category": "Life",
      "popularityIndex": 88
    },
    {
      "id": 3,
      "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
      "author": "Winston Churchill",
      "authorImage": "https://example.com/winston_churchill.jpg",
      "date": null,
      "category": "Courage",
      "popularityIndex": 92
    },
    {
      "id": 4,
      "quote": "The only limit to our realization of tomorrow will be our doubts of today.",
      "author": "Franklin D. Roosevelt",
      "authorImage": "https://example.com/franklin_roosevelt.jpg",
      "date": null,
      "category": "Inspiration",
      "popularityIndex": 89
    },
    {
      "id": 5,
      "quote": "Don't watch the clock; do what it does. Keep going.",
      "author": "Sam Levenson",
      "authorImage": "https://example.com/sam_levenson.jpg",
      "date": null,
      "category": "Motivation",
      "popularityIndex": 75
    },
    {
      "id": 6,
      "quote": "Life is really simple, but we insist on making it complicated.",
      "author": "Confucius",
      "authorImage": "https://example.com/confucius.jpg",
      "date": null,
      "category": "Life",
      "popularityIndex": 82
    },
    {
      "id": 7,
      "quote": "It does not matter how slowly you go as long as you do not stop.",
      "author": "Confucius",
      "authorImage": "https://example.com/confucius.jpg",
      "date": null,
      "category": "Persistence",
      "popularityIndex": 79
    },
    {
      "id": 8,
      "quote": "The biggest risk is not taking any risk. In a world that is changing quickly, the only strategy that is guaranteed to fail is not taking risks.",
      "author": "Mark Zuckerberg",
      "authorImage": "https://example.com/mark_zuckerberg.jpg",
      "date": "2011-07-15T09:45:00Z",
      "category": "Risk",
      "popularityIndex": 90
    },
    {
      "id": 9,
      "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
      "author": "Nelson Mandela",
      "authorImage": "https://example.com/nelson_mandela.jpg",
      "date": null,
      "category": "Resilience",
      "popularityIndex": 85
    },
    {
      "id": 10,
      "quote": "I attribute my success to this: I never gave or took any excuse.",
      "author": "Florence Nightingale",
      "authorImage": "https://example.com/florence_nightingale.jpg",
      "date": "1860-03-20T14:20:00Z",
      "category": "Success",
      "popularityIndex": 78
    },
    {
      "id": 11,
      "quote": "The best way to predict the future is to invent it.",
      "author": "Alan Kay",
      "authorImage": "https://example.com/alan_kay.jpg",
      "date": "1971-11-05T16:10:00Z",
      "category": "Innovation",
      "popularityIndex": 82
    },
    {
      "id": 12,
      "quote": "You miss 100% of the shots you don't take.",
      "author": "Wayne Gretzky",
      "authorImage": "https://example.com/wayne_gretzky.jpg",
      "date": "1991-02-18T19:30:00Z",
      "category": "Opportunity",
      "popularityIndex": 91
    },
    {
      "id": 13,
      "quote": "The harder I work, the luckier I get.",
      "author": "Samuel Goldwyn",
      "authorImage": "https://example.com/samuel_goldwyn.jpg",
      "date": null,
      "category": "Luck",
      "popularityIndex": 74
    },
    {
      "id": 14,
      "quote": "It's not what happens to you, but how you react to it that matters.",
      "author": "Epictetus",
      "authorImage": "https://example.com/epictetus.jpg",
      "date": "100-135 AD",
      "category": "Resilience",
      "popularityIndex": 79
    },
    {
      "id": 15,
      "quote": "If you want to lift yourself up, lift up someone else.",
      "author": "Booker T. Washington",
      "authorImage": "https://example.com/booker_t_washington.jpg",
      "date": "1895-09-18T08:50:00Z",
      "category": "Kindness",
      "popularityIndex": 77
    },
    {
      "id": 16,
      "quote": "The only thing necessary for the triumph of evil is for good men to do nothing.",
      "author": "Edmund Burke",
      "authorImage": "https://example.com/edmund_burke.jpg",
      "date": "1770-01-23T17:40:00Z",
      "category": "Justice",
      "popularityIndex": 76
    },
    {
      "id": 17,
      "quote": "It is during our darkest moments that we must focus to see the light.",
      "author": "Aristotle",
      "authorImage": "https://example.com/aristotle.jpg",
      "date": "384-322 BC",
      "category": "Optimism",
      "popularityIndex": 80
    },
    {
      "id": 18,
      "quote": "If you don't stand for something, you will fall for anything.",
      "author": "Malcolm X",
      "authorImage": "https://example.com/malcolm_x.jpg",
      "date": "1964-12-10T14:55:00Z",
      "category": "Principles",
      "popularityIndex": 83
    },
    {
      "id": 19,
      "quote": "The future belongs to those who believe in the beauty of their dreams.",
      "author": "Eleanor Roosevelt",
      "authorImage": "https://example.com/eleanor_roosevelt.jpg",
      "date": "1936-05-30T11:25:00Z",
      "category": "Dreams",
      "popularityIndex": 87
    },
    {
      "id": 20,
      "quote": "Life is either a daring adventure or nothing at all.",
      "author": "Helen Keller",
      "authorImage": "https://example.com/helen_keller.jpg",
      "date": "1940-07-05T13:05:00Z",
      "category": "Adventure",
      "popularityIndex": 84
    }
  ]