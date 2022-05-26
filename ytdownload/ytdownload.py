# Ian Royer
# 6-1-2021
# A simple downloader for youtube videos

from pytube import YouTube

class Ytdownloader:
    ytclass = YouTube
    dl_loc = ""

    def __init__(self, link = None, loc = None):
        self.ytclass = link
        self.dl_loc = loc


    def getinfo(self):
        '''
        Gets some information about the information set in pytube
        
        Return:
            A single string of pertinent information about the video that has been set
        '''
        form_info = ("Title: " + self.ytclass.title + "\n"
        + "Author: " + self.ytclass.author + "\n"
        + "Views: " + str(self.ytclass.views) + "\n"
        + "Length: " + str(self.ytclass.length//60) + "m " + str(self.ytclass.length%60) + "s\n\n")

        return form_info
    
    def setLink(self, link):
        '''
        Sets the link to be downloaded by the pytube class
        
        Arguments:
            link    -string of the url to be used
        
        Return:
            True when successful, false otherwise
        '''
        try:
            self.ytclass = YouTube(link)
        except:
            #print("Error in setting link")
            self.ytclass = None
            return False
        else:
            return True
    
    def setLoc(self, loc):
        '''
        Sets the location to be downloaded to by pytube
        
        Arguments:
            self    --Ytdownloader\n
            loc     --file path to be downloaded to
        '''
        self.dl_loc = loc

    def do_download(self):
        '''
        Downloads a video from the set url to the set location
        
        Return:
            True when successful, false otherwise
        '''
        try:
            ytstream = self.ytclass.streams.get_highest_resolution()
            ytstream.download(self.dl_loc)
        except:
            return False
        else:
            return True

    def check_avail(self):
        '''
        Checks if the available to be download (ie. is able to be downloaded) 

        Return:
            True when available, false otherwise
        '''
        try:
            self.ytclass.check_availability()
        except:
            return False
        else:
            return True
