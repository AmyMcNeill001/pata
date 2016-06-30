#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2, json

json_str = """
    [{"Name":"East Road","Stations":["Grey Havens","Tower Hills","Far Downs","White Downs","Michel Delving","Hobbiton","Buckland","Old Forest","Barrow Downs","Bree","Midgewater Marshes","Weathertop","Last Bridge","Fords of Bruinen","Rivendell"]},{"Name":"Mirkwood Circle","Stations":["Caras Galadon","Gladden Fields","Old Ford","The Carrock","Rhimdath Crossing","Framburg","Elvenking's Halls","Esgaorth","Dale","Erebor"]},{"Name":"Misty Mountain Way","Stations":["Lond Daer","Tharbad","Ost-in-Edhil","Gate of Moria","Moria","Mirromere","Lorien Forest","Caras Galadon","Dol Guldur"]},{"Name":"Rohan Railroad","Stations":["Minas Tirith","Duradan Forest","Firienholt","Edoras","Helm's Deep","Fords of Isen","Isengard","Fangorn Forest","Field of Celebrant","Caras Galadon"]},{"Name":"Gondor Limited","Stations":["Dol Amroth","Edhellond","Calembel","Ethring","Linhir","Pelargir","Emyn Arnen","Minas Tirith"]},{"Name":"Mordor Monorail","Stations":["Minas Tirith","Osgiliath","Minas Morgul","Mount Doom","Barad-dûr"]},{"Name":"Green Way","Stations":["Michel Delving","Sarn Ford","Tharbad","Fords of Isen"]}]
    """

html_form = """<html>
    <head>
    <meta charset = "utf-8"/>
    <title>Don't Go to Mordor!</title>
    </head>
    <body style="margin: 10%">
    <p align="center"><h1>Lord of the Rings</h1></p>
    <form>
    <div style="width:40%;float:left;display:inline-block;">
    From:   <br><select name="from" type="text">
				<option disabled>- - - - - - -	</option>
                <option disabled>	East Road</option>
                <option disabled>- - - - - - -	</option>
                <option>Grey Havens</option>
                <option>Tower Hills</option>
                <option>Far Downs</option>
                <option>White Downs</option>
                <option>Michel Delving</option>
                <option>Hobbiton</option>
                <option>Buckland</option>
                <option>Old Forest</option>
                <option>Barrow Downs</option>
                <option>Bree</option>
                <option>Midgewater Marhes</option>
                <option>Weathertop</option>
                <option>Last Bridge</option>
                <option>Fords of Bruinen</option>
                <option>Rivendell</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Merkwood Circle</option>
                <option disabled>- - - - - - -	</option>
                <option>Caras Galadon</option>
                <option>Gladden fields</option>
                <option>Old Ford</option>
                <option>The Carrock</option>
                <option>Rhindath Crossing</option>
                <option>Framburg</option>
                <option>Elvenking's Halls</option>
                <option>Esgaorth</option>
                <option>Dale</option>
                <option>Erebor</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Misty Mountain Way</option>
                <option disabled>- - - - - - -	</option>
                <option>Lond Daer</option>
                <option>Tharbad</option>
                <option>Ost-in-Edhil</option>
                <option>Gate of Moria</option>
                <option>Moria</option>
                <option>Mirromere</option>
                <option>Lorien Forest</option>
                <option>Caras Galadon</option>
                <option>Dol Guldur</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Rohan Railroad</option>
                <option disabled>- - - - - - -	</option>
                <option>Minas Tirith</option>
                <option>Duradan Forest</option>
                <option>Firienholt</option>
                <option>Edoras</option>
                <option>Helm's Deep</option>
                <option>Fords of Isen</option>
                <option>Isengard</option>
                <option>Fangorn Forest</option>
                <option>Caras Galadon</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Gondor Limited</option>
                <option disabled>- - - - - - -	</option>
                <option>Dol Amroth</option>
                <option>Edhellond</option>
                <option>Calembel</option>
                <option>Linhir</option>
                <option>Pelargir</option>
                <option>Emyn Arnen</option>
                <option>Minas Tirith</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Mordor Monorail</option>
                <option disabled>- - - - - - -	</option>
                <option>Minas Tirith</option>
                <option>Osgiliath</option>
                <option>Minas Morgul</option>
                <option>Mount Doom</option>
                <option>Barad-dûr</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Green Way</option>
                <option disabled>- - - - - - -	</option>
                <option>Michel Delving</option>
                <option>Sarn Ford</option>
                <option>Tharbad</option>
                <option>Fords of Isen</option>
                </select>
                </div>
                <div>
            To: <br> <select name="to" type="text">
                <option disabled>- - - - - - -	</option>
                <option disabled>	East Road</option>
                <option disabled>- - - - - - -	</option>
                <option>Grey Havens</option>
                <option>Tower Hills</option>
                <option>Far Downs</option>
                <option>White Downs</option>
                <option>Michel Delving</option>
                <option>Hobbiton</option>
                <option>Buckland</option>
                <option>Old Forest</option>
                <option>Barrow Downs</option>
                <option>Bree</option>
                <option>Midgewater Marhes</option>
                <option>Weathertop</option>
                <option>Last Bridge</option>
                <option>Fords of Bruinen</option>
                <option>Rivendell</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Merkwood Circle</option>
                <option disabled>- - - - - - -	</option>
                <option>Caras Galadon</option>
                <option>Gladden fields</option>
                <option>Old Ford</option>
                <option>The Carrock</option>
                <option>Rhindath Crossing</option>
                <option>Framburg</option>
                <option>Elvenking's Halls</option>
                <option>Esgaorth</option>
                <option>Dale</option>
                <option>Erebor</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Misty Mountain Way</option>
                <option disabled>- - - - - - -	</option>
                <option>Lond Daer</option>
                <option>Tharbad</option>
                <option>Ost-in-Edhil</option>
                <option>Gate of Moria</option>
                <option>Moria</option>
                <option>Mirromere</option>
                <option>Lorien Forest</option>
                <option>Caras Galadon</option>
                <option>Dol Guldur</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Rohan Railroad</option>
                <option disabled>- - - - - - -	</option>
                <option>Minas Tirith</option>
                <option>Duradan Forest</option>
                <option>Firienholt</option>
                <option>Edoras</option>
                <option>Helm's Deep</option>
                <option>Fords of Isen</option>
                <option>Isengard</option>
                <option>Fangorn Forest</option>
                <option>Caras Galadon</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Gondor Limited</option>
                <option disabled>- - - - - - -	</option>
                <option>Dol Amroth</option>
                <option>Edhellond</option>
                <option>Calembel</option>
                <option>Linhir</option>
                <option>Pelargir</option>
                <option>Emyn Arnen</option>
                <option>Minas Tirith</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Mordor Monorail</option>
                <option disabled>- - - - - - -	</option>
                <option>Minas Tirith</option>
                <option>Osgiliath</option>
                <option>Minas Morgul</option>
                <option>Mount Doom</option>
                <option>Barad-dûr</option>
                <option disabled>- - - - - - -	</option>
                <option disabled>	Green Way</option>
                <option disabled>- - - - - - -	</option>
                <option>Michel Delving</option>
                <option>Sarn Ford</option>
                <option>Tharbad</option>
                <option>Fords of Isen</option>
                </select>
                </div>
                <br>
                <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p><button type="submit">Take Me There!</button>
                </form>
                </body>
                </html> 
"""

data = json.loads(json_str)

def makeMap(data):
    graph = {}
    for line_stations_map in data:
        eki_list = line_stations_map['Stations']
        for i, eki in enumerate(eki_list):
            if eki not in graph:
                graph[eki] = []
            for j in (i-1, i+1):
                if 0 <= j < len(eki_list):
                    graph[eki].append(eki_list[j])
    return graph

def makeRoute(graph, start, end, route=[]):
    route = route + [start]
    if start == end:
        return route
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in route:
            newroute = find_route(graph, node, end, route)
            if newroute: return newroute
    return None

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(html_form)
    def post(self):
        start = self.request.get("from")
        end = self.request.get("to")
        self.response.write("From: " + start + " To: "+ end + "<br>")
        route = makeRoute(makeMap(data), start, end)
        for station in route:
            self.response.write(station + " to")

app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ], debug=True)

