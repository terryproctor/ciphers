#!/usr/bin/env python
# coding: utf-8

# # Casual Coded Correspondence: The Project
# 
# In this project, you will be working to code and decode various messages between you and your fictional cryptography enthusiast pen pal Vishal. You and Vishal have been exchanging letters for quite some time now and have started to provide a puzzle in each one of your letters.  Here is his most recent letter:
# 
#      Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a  Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. For example, if I chose an offset of 3 and a message of "hello", I would code my message by shifting each letter 3 places to the left (with respect to the alphabet). So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". Then I have my coded message,"ebiil"! Now I can send you my message and the offset and you can decode it. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer coded message that you have to decode yourself!
#     
#         xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
#     
#     This message has an offset of 10. Can you decode it?
#     
# 
# #### Step 1: Decode Vishal's Message
# In the cell below, use your Python skills to decode Vishal's message and print the result. Hint: you can account for shifts that go past the end of the alphabet using the modulus operator, but I'll let you figure out how!

# In[1]:


punctuation = (",", ".", "!", "?", "'")


# In[2]:


def decrypt(message, offset):
    split_message = message.split(" ")
    ascii_words = []
    for word in split_message:
        x = [letter if letter in punctuation else ord(letter) for letter in word]
        ascii_words.append(x)
    new_ascii_words = []
    for word in ascii_words:
        word = [num if (num in punctuation) else chr(num + offset) if (num+offset <= 122) else chr(num + offset -26) for num in word]
        new_ascii_words.append("".join(word))
    return (" ".join(new_ascii_words))


# In[3]:


message1 = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'


# In[4]:


print(decrypt(message1, 10))


# #### Step 2: Send Vishal a Coded Message
# Great job! Now send Vishal back a message using the same offset. Your message can be anything you want! Remember, coding happens in opposite direction of decoding.

# In[5]:


def crypt(message, offset):
    split_message = message.split(" ")
    ascii_words = []
    for word in split_message:
        x = [letter if letter in punctuation else ord(letter) for letter in word]
        ascii_words.append(x)
    new_ascii_words = []
    for word in ascii_words:
        word = [num if (num in punctuation) else chr(num - offset) if (num-offset >= 96) else chr(num - offset + 26) for num in word]
        new_ascii_words.append("".join(word))
    return (" ".join(new_ascii_words))
    


# In[6]:


message2 = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"


# In[7]:


print(crypt(message2, 10))


# #### Step 3: Make functions for decoding and coding 
# 
# Vishal sent over another reply, this time with two coded messages!
#     
#     You're getting the hang of this! Okay here are two more messages, the first one is coded just like before with  an offset of ten, and it contains the hint for decoding the second message!
#     
#     First message:
#     
#         jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.
#         
#     Second message:
#     
#         bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!
#     
# Decode both of these messages. 
# 
# If you haven't already, define two functions `decoder(message, offset)` and `coder(message, offset)` that can be used to quickly decode and code messages given any offset.

# In[8]:


first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(decrypt(first_message, 10))


# In[9]:


second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(decrypt(second_message, 14))


# #### Step 4: Solving a Caesar Cipher without knowing the shift value
# 
# Awesome work! While you were working to decode his last two messages, Vishal sent over another letter! He's really been bitten by the crytpo-bug. Read it and see what interesting task he has lined up for you this time.
# 
#             Hello again friend! I knew you would love the Caesar Cipher, it's a cool simple way to encrypt messages. Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? That's all changed with computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.
#             
#             To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of   the shift. You'll have to brute force it yourself.
#             
#             Here's the coded message:
#             
#             vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
#             
#             Good luck!
#             
# Decode Vishal's most recent message and see what it says!

# In[10]:


message_3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."


# In[11]:


for i in range(27):
    print(f"offset {i}:", decrypt(message_3, i))


# In[12]:


offest_3 = 7


# #### Step 5: The Vigenère Cipher
# 
# Great work! While you were working on the brute force cracking of the cipher, Vishal sent over another letter. That guy is a letter machine!
# 
#             Salutations! As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. This next cipher I'm going to teach you is the Vigenère Cipher, invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.
#             
#            The Vigenère Cipher is a polyalphabetic substitution cipher, as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.
#            
#            Consider the message
#            
#                barry is the spy
# 
#            If we want to code this message, first we choose a keyword. For this example, we'll use the keyword
#            
#                dog
#                
#            Now we use the repeat the keyword over and over to generate a _keyword phrase_ that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our _keyword phrase_ is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift the each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth. Remember, we zero-index because this is Python we're talking about!
# 
#                         message:       b  a  r  r  y    i  s   t  h  e   s  p  y
#                 
#                  keyword phrase:       d  o  g  d  o    g  d   o  g  d   o  g  d
#                  
#           resulting place value:       4  14 15 12 16   24 11  21 25 22  22 17 5
#       
#             So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth. Once we complete all the shifts we end up with our coded message:
#             
#                 eoxum ov hnh gvb
#                 
#             As you can imagine, this is a lot harder to crack without knowing the keyword! So now comes the hard part. I'll give you a message and the keyword, and you'll see if you can figure out how to crack it! Ready? Okay here's my message:
#             
#                 dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!
#                 
#             and the keyword to decode my message is 
#             
#                 friends
#                 
#             Because that's what we are! Good luck friend!
#            
# And there it is. Vishal has given you quite the assignment this time! Try to decode his message. It may be helpful to create a function that takes two parameters, the coded message and the keyword and then work towards a solution from there.
# 
# **NOTE:** Watch out for spaces and punctuation! When there's a space or punctuation mark in the original message, there should be a space/punctuation mark in the corresponding repeated-keyword string as well! 

# In[13]:


message_4 = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword_1 = "friends"


# In[14]:


punctuation2 = (",", ".", "!", "?", "'", " ")


# In[37]:


def decrypt_vcipher(message, keyword):
    # create a list of what each letter should be offset by depending on it's postion
    offsets = [ord(x) - 97 for x  in keyword]
    
    new_message = ""
    ################################
    # function to decrypt each letter
    def decrypt_char(letter, offset):
        #skip punctuation
        if letter in punctuation2:
            return letter
        else:
            x = ord(letter)

        if (x - offset >= 96):
            x = chr(x - offset)
        else:
            x = chr(x - offset + 26)
        return x
    ##################################
    # to discount spaces a for loop needs to exclude punctuation and so needs to be shorter by how many times punctuation appears
    skipped = 0
    
    for i in range(len(message)):
        if message[i] in punctuation2:
            new_message += message[i]
            skipped += 1
            continue
        else:
            off_by = offsets[(i - skipped) % len(offsets)]
            new_message += decrypt_char(message[i], off_by)

    return new_message
    
    


# In[38]:


decrypt_vcipher(message_4, keyword_1)


# #### Step 6: Send a message with the  Vigenère Cipher
# Great work decoding the message. For your final task, write a function that can encode a message using a given keyword and write out a message to send to Vishal!
# 
# *As a bonus, try calling your decoder function on the result of your encryption function. You should get the original message back!*

# In[39]:


def crypt_vcipher(message, keyword):
    # create a list of what each letter should be offset by depending on it's postion
    offsets = [ord(x) - 97 for x  in keyword]
    new_message = ""
    
    def crypt_char(letter, offset):
        #skip punctuation
        if letter in punctuation2:
            return letter
        else:
            x = ord(letter)

        if (x + offset <= 122):
            x = chr(x + offset)
        else:
            x = chr(x + offset - 26)
        return x
    
        # to discount spaces a for loop needs to exclude punctuation and so needs to be shorter by how many times punctuation appears
    skipped = 0
    
    for i in range(len(message)):
        if message[i] in punctuation2:
            new_message += message[i]
            skipped += 1
            continue
        else:
            off_by = offsets[(i - skipped) % len(offsets)]
            new_message += crypt_char(message[i], off_by)

    return new_message
    


# In[40]:


message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

print(crypt_vcipher(message_for_v,keyword))
sent_message = crypt_vcipher(message_for_v,keyword)


# In[41]:


print(decrypt_vcipher(sent_message,keyword))


# #### Conclusion
# Over the course of this project you've learned about two different cipher methods and have used your Python skills to code and decode messages. There are all types of other facinating ciphers out there to explore, and Python is the perfect language to implement them with, so go exploring! 
