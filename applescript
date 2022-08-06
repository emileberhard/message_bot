on run {input, parameters}
tell application "Messages"
    set targetBuddy to "(070) 817-1177"
    set targetService to id of 1st account whose service type = SMS
    set textMessage to (item 1 of input)
    set theBuddy to participant targetBuddy of account id targetService
    send textMessage to theBuddy
end tell
return input
end run