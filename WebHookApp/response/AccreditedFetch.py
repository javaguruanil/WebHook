class AccreditedFetch():
    def __init__(self
                 , _id
                 , borough
                 , subject
                 , possible_options
                 , where_to_find_more
                 , create_date
                 , update_date
                 , soft_delete):
        self._id = _id
        self.borough = borough
        self.subject = subject
        self.possible_options = possible_options
        self.where_to_find_more = where_to_find_more
