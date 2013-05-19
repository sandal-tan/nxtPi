//
//  AppDelegate.h
//  RemoteC
//
//  Created by Ian Baldwin on 5/19/13.
//  Copyright (c) 2013 Elektrik Fish. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface AppDelegate : NSObject <NSApplicationDelegate>

@property (assign) IBOutlet NSWindow *window;
IBOutlet NSTextField *myLabel;
}
- (IBAction)myAction:(id)sender;
@end

@end
