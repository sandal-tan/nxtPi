--
--  AppDelegate.applescript
--  Remote
--
--  Created by Ian Baldwin on 5/19/13.
--  Copyright (c) 2013 Elektrik Fish. All rights reserved.
--

script AppDelegate
	property parent : class "NSObject"
    property lightButton : missing value
    property connectButton : missing value
    property theLabel1 : missing value
    property lightLabel : missing value
	property CWInterface : class "CWInterface"
    
	on applicationWillFinishLaunching_(aNotification)
		set title of lightButton to "On"
        set title of connectButton to "Connect"
        theLabel1's setStringValue_("Not Connected")
        lightLabel's setStringValue_("Off")
	end applicationWillFinishLaunching_
    
    on connectToPiBot_(aNotification)
        set title of connectButton to "Connecting..."
        set currentInterface to CWInterface's interface()
        set networks to currentInterface's scanForNetworksWithName_error_(missing value, missing value)
        set networkNames to networks's valueForKey_("ssid")'s allObjects() as list
        if networkNames contains "PiBot"
        theLabel1's setStringValue_("PiBot Found, Connecting...")
        do shell script ("networksetup -setairportnetwork en1 PiBot aaaaa11111")
        theLabel1's setStringValue_("Connected")
        set title of connectButton to "Disconnect"
        else
        theLabel1's setStringValue_("PiBot Not Found")
        end if
    end connectToPiBot_
        
	
	on applicationShouldTerminate_(sender)
		-- Insert code here to do any housekeeping before your application quits 
		return current application's NSTerminateNow
	end applicationShouldTerminate_
	
end script