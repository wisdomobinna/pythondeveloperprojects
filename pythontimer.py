class Timer:
    def __init__(self, hh, mm, ss):
        #
        self.hh = hh
        self.mm = mm
        self.ss = ss
        #

    def __str__(self):
        return f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}"
        #
    def next_second(self):
        #
        if self.ss == 59:
            self.ss = 0
            if self.mm == 59:
                self.mm = 0
                if self.hh  == 23:
                    self.hh = 0
                elif self.hh < 23:
                    self.hh += 1
            elif self.mm < 59:
                self.mm += 1
        elif self.ss < 59:
            self.ss =+ 1
        
        return Timer(self.hh, self.mm, self.ss)
            
            
    def prev_second(self):
        #
        if self.ss == 0:
            self.ss = 59
            if self.mm == 0:
                self.mm = 59
                if self.hh  == 0:
                    self.hh = 23
                elif self.hh > 0:
                    self.hh -= 1
            elif self.mm > 0:
                self.mm -= 1
        elif self.ss > 0:
            self.ss -= 1
        
        return Timer(self.hh, self.mm, self.ss)


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    
