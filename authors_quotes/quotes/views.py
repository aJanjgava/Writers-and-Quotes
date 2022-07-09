from django.shortcuts import render
from django.http import Http404 ,HttpResponseRedirect


authors_and_quotes = {
    "Albert Camus": ["I looked up at the mass of signs and stars in the night sky and laid myself open for the first time to the benign indifference of the world.", "The Stranger"],
    "Dante Alighieri": ["The devil is not as black as he is painted.", "The Divine Comedy"],
    "Edgar Allan Poe":["Those who dream by day are cognizant of many things which escape those who dream only by night.","Eleonora"],
    "Franz Kafka":["Logic may indeed be unshakeable, but it cannot withstand a man who is determined to live.","The Trial"],
    "Fyodor Dostoyevsky":["What is hell? I maintain that it is the suffering of being unable to love.", "The Brothers Karamazov"],
    "George Orwell":["The best books... are those that tell you what you know already.", "1984"],
    "Johann Goethe":["As soon as you trust yourself, you will know how to live.","Faust"],
    "Laozi":["The journey of a thousand miles begins with a single step.","Tao Te Ching"], 
    "Leo Tolstoy":["We can know only that we know nothing. And that is the highest degree of human wisdom.","War and Peace"],
    "Miguel De Cervantes":["The truth may be stretched thin, but it never breaks, and it always surfaces above lies, as oil floats on water.","Don Quixote"],
    "Niccolo Machiavelli":["Everyone sees what you appear to be, few experience what you really are.","The Prince"],
    "Paulo Coelho":["And, when you want something, all the universe conspires in helping you to achieve it.","The Alchemist"], 
    "Ryunosuke Akutagawa":["I could wish for nothing more than to die for a childish dream in which I truly believed.","Mandarins"],
    "Sun-Tzu":["Appear weak when you are strong, and strong when you are weak.", "The Art of War"], 
    "Victor Hugo":["Even the darkest night will end and the sun will rise.", "Les Misérables"], 
    "William Shakespeare":["There is nothing either good or bad, but thinking makes it so.","Hamlet"]
}

books_and_covers = {
    "Albert Camus": "Albert-Camus.jpg",
    "Dante Alighieri": "Dante-Alighieri.jpg",
    "Edgar Allan Poe":"Edgar-Allanpo.jpg",
    "Franz Kafka":"Franz-Kafka.jpg",
    "Fyodor Dostoyevsky":"Fyodor-Dostoyevsky.jpg",
    "George Orwell":"George-Orwell.jpg",
    "Johann Goethe":"Johann-Goethe.jpg",
    "Laozi":"Laozi.jpg", 
    "Leo Tolstoy":"Leo-Tolstoy.jpg",
    "Miguel De Cervantes":"Miguel-DeCervantes.jpg",
    "Niccolo Machiavelli":"Niccolo-Machiavelli.jpg",
    "Paulo Coelho":"Paulo-Coelho.jpg", 
    "Ryunosuke Akutagawa":"Ryunosuke-Akutagawa.jpg",
    "Sun-Tzu":"Sun-Tzu.jpg", 
    "Victor Hugo":"Victor-Hugo.jpg", 
    "William Shakespeare":"William-Shakespeare.jpg"
}


# Create your views here.

def writers(request):
    author_names = list(authors_and_quotes.keys())

    return render(request, 'quotes/writers.html', {
        'author_names': author_names
    })


def quote(request, name):
    quote = authors_and_quotes[name][0]
    book_name = authors_and_quotes[name][1]
    cover = books_and_covers[name]
    return render(request, 'quotes/quotes.html', {
        'book_name': book_name,
        'quote': quote,
        'cover': cover,
    })
    

def quote_by_number(request, name):
    try:
        author_names = list(authors_and_quotes.keys())
        redirect_name = author_names[name-1]
        return HttpResponseRedirect(redirect_name)
    except:
        raise Http404


