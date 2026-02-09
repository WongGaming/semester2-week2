"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    query = '''
            Select films.title, screenings.screen, tickets.price from films, screenings, tickets, customers
            Where customers.customer_id = ? and tickets.customer_id = customers.customer_id and screenings.screening_id = tickets.screening_id and films.film_id = screenings.film_id
            Order By films.title Asc;
            '''
    cursor = conn.execute(query, (customer_id,))
    return cursor.fetchall()
    


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    query = '''
            Select screenings.screening_id, films.title, count(tickets.ticket_id) from screenings
            Join films on films.film_id = screenings.film_id
            Left Join tickets on tickets.screening_id = screenings.screening_id
            LEFT JOIN customers ON customers.customer_id = tickets.customer_id
            Group By screenings.screening_id
            Order by count(tickets.ticket_id) Desc, screenings.screening_id asc;
            '''
    cursor = conn.execute(query)
    return cursor.fetchall()


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    query = '''
            Select customers.customer_name, sum(tickets.price) from customers
            Join tickets on tickets.customer_id = customers.customer_id
            Group By customers.customer_id
            Having sum(tickets.price) > 0
            Order By sum(tickets.price) desc
            limit ?
            '''
    cursor = conn.execute(query, (limit,))
    return cursor.fetchall()