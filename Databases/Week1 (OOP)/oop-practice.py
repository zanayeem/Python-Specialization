class Nayeem:
    #Attributes
    height = 1.93
    weight = 62
    age = 24
    github_user = "zanayeem"
    facebook_user = "zzz.nayeem"
    instagram_user = "zanayeem"
    program_skill = ["Java","C+","Python","HTML/CSS","JS","Bootstrap","AJAX","PhP"]
    #Methods
    def __init__(self,*z): #Constructor #  "*" followed by a variable parameter can or cannot exist.
        print(*z,"I am constructed lol")
        
    def physique(self): #SELF Means its own class attributes
       print("Height is ",self.height,"metres Weight is ",Nayeem.weight,"kgs")
    
    def githubProfile(self):
        print("www.github.com/"+ self.github_user)
    
    def socialMedia(self, media ): #always need to send with self any other parameters
        if media == "facebook" or media == "fb":
            print("www.facebook.com/"+ Nayeem.facebook_user)
        elif media == "instagram" or media == "ig": 
            print("www.instagram.com/"+ Nayeem.instagram_user)
        else:
            print("Provide proper platforms")
class NayeemSkills(Nayeem): #Inheritance class of Nayeem
    
    def programSkills(self):
        j = 1 #Local variables
        print("The list of skills:")
        for i in  Nayeem.program_skill: #Inheriting "program skill" from Nayeem class            
            print(j,".",i)
            j=j+1

#----------------------------------------------------------------------------------------#    
#OBJECTS OR INSTANCES

zn = Nayeem() #Instantiating

zn.physique() #Calling methods of instances
zn.githubProfile()
zn.socialMedia("fb")

nay = Nayeem("YEAYY!") #Passing the arguement to the constructor with *variable
naynay = NayeemSkills()
naynay.programSkills()



 
                