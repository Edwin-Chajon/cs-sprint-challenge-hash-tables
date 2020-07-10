#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    route = []
    trip_tickets = {}

# loop through tickets and set the destinations for each of them
    for ticket in tickets:
        # add all tickets to trip_tickets source and destination
        trip_tickets[ticket.source] = ticket.destination
    # next stop for 'NONE'
    next_stop = trip_tickets['NONE']

# as long as next stop is not 'NONE'
    while next_stop != 'NONE':
        # add thee next stop to the route
        route.append(next_stop)
        #next stop will be taken from trip_tickets at the index of next_stop
        next_stop = trip_tickets[next_stop]
    #finalize the trip once all conditions are met with 'NONE'
    route.append('NONE')

    return route