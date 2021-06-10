        if loan < 1:
            loan = 100
            self.screen.ids.loan.text = str(loan)
        if months < 1:
            months = 1
            self.screen.ids.months.text = str(months)
        if interest < 1:
            interest = 1
            self.screen.ids.interest.text = str(interest)
