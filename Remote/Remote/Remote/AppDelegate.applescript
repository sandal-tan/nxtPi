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
    property theLabel1 : missing value
    property lightLabel : missing value
	property CWInterface : class "CWInterface"
    
	on applicationWillFinishLaunching_(aNotification)
		set title of lightButton to "On"
        theLabel1's setStringValue_("Not Connected")
        lightLabel's setStringValue_("Off")
	end applicationWillFinishLaunching_
    
    on connectToPiBot_(aNotification)
        theLabel1's setStringValue_("Looking for PiBot...")
        set currentInterface to CWInterface's interface()
        set networks to currentInterface's scanForNetworksWithName_error_(missing value, missing value)
        set networkNames to networks's valueForKey_("ssid")'s allObjects() as list
        log networkNames
        if networkNames contains "PiBot"
        say "Network Found"
        theLabel1's setStringValue_("Connecting")
        else
        say "No NetWork Found"
        theLabel1's setStringValue_("Not Connected")
        end if
    end connectToPiBot_
        
	
	on applicationShouldTerminate_(sender)
		-- Insert code here to do any housekeeping before your application quits 
		return current application's NSTerminateNow
	end applicationShouldTerminate_
	
end script