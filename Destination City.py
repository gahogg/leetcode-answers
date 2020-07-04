class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_set = set()

        for (outgoing_city, _) in paths:
            outgoing_set.add(outgoing_city)

        for (_, incoming_city) in paths:
            if incoming_city not in outgoing_set:
                return incoming_city