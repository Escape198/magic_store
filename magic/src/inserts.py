from datetime import date

from src import db
from src.models import Book


def populate_books():
    harry_potter_and_ph_stone = Book(
        title='Harry Potter and the Philosopher\'s Stone',
        release_date=date(1997 , 6, 26),
        description='The first novel in the Harry Potter series and Rowling\'s debut novel, it follows Harry Potter, a young wizard who discovers his magical heritage on his eleventh birthday, when he receives a letter of acceptance to Hogwarts School of Witchcraft and Wizardry.',
        distributed_by='Bloomsbury',
        pages=223,
        rating=7.6,
    )
    harry_potter_and_ch_s = Book(
        title='Harry Potter and Chamber of Secrets',
        release_date=date(1998, 7, 2),
        description='The plot follows Harry\'s second year at Hogwarts School of Witchcraft and Wizardry, during which a series of messages on the walls of the school's corridors warn that the "Chamber of Secrets" has been opened and that the "heir of Slytherin" would kill all pupils who do not come from all-magical families.',
        distributed_by='Bloomsbury',
        pages=251,
        rating=7.4,
    )
    harry_potter_and_priz_az = Book(
        title='Harry Potter and the Prizoner of Azkaban',
        release_date=date(1999, 7, 8),
        description='The book follows Harry Potter, a young wizard, in his third year at Hogwarts School of Witchcraft and Wizardry.',
        distributed_by='Bloomsbury',
        pages=317 ,
        rating=7.9,
    )
    harry_potter_and_ph_goblet_fire = Book(
        title='Harry Potter and the Goblet of Fire',
        release_date=date(2000, 7, 8),
        description='Harry Potter finds himself competing in a hazardous tournament between rival schools of magic, but he is distracted by recurring nightmares.',
        distributed_by='Bloomsbury',
        pages=636,
        rating=7.7,
    )
    harry_potter_and_order_phoenix = Book(
        title='Harry Potter and the Order of the Phoenix',
        release_date=date(2003, 6, 21),
        description='With their warning about Lord Voldemort\'s (Ralph Fiennes\') return scoffed at, Harry (Daniel Radcliffe) and Dumbledore (Sir Michael Gambon) are targeted by the Wizard authorities as an authoritarian bureaucrat slowly seizes power at Hogwarts.',
        distributed_by='Bloomsbury',
        pages=766,
        rating=7.5,
    )
    harry_potter_and_half_blood_prince = Book(
        title='Harry Potter and the Half-Blood Prince',
        release_date=date(2005, 7, 16),
        description='As Harry Potter (Daniel Radcliffe) begins his sixth year at Hogwarts, he discovers an old book marked as "the property of the Half-Blood Prince" and begins to learn more about Lord Voldemort\'s (Ralph Fiennes\') dark past.',
        distributed_by='Bloomsbury',
        pages=607,
        rating=7.6,
    )
    harry_potter_and_deathly_hallows_2 = Book(
        title='Harry Potter and the Deathly Hallows',
        release_date=date(2007 , 7, 14),
        description='Harry, Ron, and Hermione search for Voldemort\'s remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.',
        distributed_by='Bloomsbury'ы,
        pages=130,
        rating=8.1,
    )

    db.session.add(harry_potter_and_ph_stone)
    db.session.add(harry_potter_and_ch_s)
    db.session.add(harry_potter_and_priz_az)
    db.session.add(harry_potter_and_ph_goblet_fire)
    db.session.add(harry_potter_and_order_phoenix)
    db.session.add(harry_potter_and_half_blood_prince)
    db.session.add(harry_potter_and_deathly_hallows_1)
    db.session.add(harry_potter_and_deathly_hallows_2)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Populating db...')
    populate_books()
    print('Successfully populated!')
