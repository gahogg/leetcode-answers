class Groups_dict:

    def __init__(self):
        self.dict = {}

    def __setitem__(self, group_size, iD):
        if group_size in self.dict:
            groups = self.dict[group_size]
            group_index = groups[0]
            groups[group_index].append(iD)

            if len(groups[group_index]) > group_size:
                groups.append([groups[group_index].pop()])
                groups[0] += 1
        else:
            self.dict[group_size] = [1, [iD]]

    def get_groups(self):
        ret_lst = []

        for key in self.dict.keys():
            for group in self.dict[key][1:]:
                ret_lst.append(group)

        return ret_lst


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_dict = Groups_dict()

        for iD, group_size in enumerate(groupSizes):
            groups_dict[group_size] = iD

        return groups_dict.get_groups()