from haystack.forms import SearchForm


class EntriesSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()