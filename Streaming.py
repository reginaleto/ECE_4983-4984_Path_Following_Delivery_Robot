# import picamera2 -- only works on Linux
import wx


class Streaming_GUI(wx.Frame): 
    window = (1280, 760)
    def __init__(self, parent, title="Path Following Delivery Robot - Stream"):
        super(Streaming_GUI, self).__init__(parent)
        
        self.Start = wx.Button()
        
        self.Bind(wx.EVT_BUTTON, self.Start_System)
        
    
    def Start_System( self, event ):
        event.Skip()