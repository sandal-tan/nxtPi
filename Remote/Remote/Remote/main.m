//
//  main.m
//  Remote
//
//  Created by Ian Baldwin on 5/19/13.
//  Copyright (c) 2013 Elektrik Fish. All rights reserved.
//

#import <Cocoa/Cocoa.h>

#import <AppleScriptObjC/AppleScriptObjC.h>

int main(int argc, char *argv[])
{
    [[NSBundle mainBundle] loadAppleScriptObjectiveCScripts];
    return NSApplicationMain(argc, (const char **)argv);
}
