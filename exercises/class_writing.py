
"""Define the Profile class."""

#Write a class profile 
class profile:

    #It should have two attributes, username: str and private: bool
    username: str 
    private: bool

    def _int_(self, username_input: str):
        self.username = username_input 
        self.private = True 

    def tweet(slef, msg: str) -> None:
        if self.private == False:
            print(msg)