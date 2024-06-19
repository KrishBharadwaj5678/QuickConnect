import pywhatkit
import streamlit as st
import datetime

st.set_page_config(
    page_title="QuickConnect",
    page_icon="data:image/jpeg;base64,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",
    menu_items={
        "About":"""Send WhatsApp messages directly from our website with just a few clicks! Connect instantly with friends and family using QuickConnect's seamless interface."""
    }
)

st.write("<h2 style='color:#25D366';> Instant WhatsApp Messaging</h2>",unsafe_allow_html=True)

st.write("<img src='https://cdn.gencraft.com/prod/user/9b58dce4-d38a-4d53-8f59-5326387b0c95/89e7282d-1d94-4cd0-937e-f070a8153e83/image/image0_0.jpg?Expires=1726514198&Signature=msKsepzuz4tjWrJ3RjM0LPVSYhD834MESe2HJjVDs-vbHniRbqR6mbeZZ-HAdPwVc3RsBZazCCyT2rUKsTmlNg5ys7VHUy8J8aL7taKuiGIeaGgkbYQMBuFPDrRUfnQWQqkKM148Xml3qwAOvrKcoQKf3awSfMQBni-uko1iVv76-dLKxn6VMhrChjfkYz-FmN3UQSuxAsvHBe3QMk3aeljJ7JsdCkuGufnhsG5LIvpjzS8ccy~7PxO2bTrCpOC1NwmBDWGg~uDAovwv0hoJ4o9F~c2cejifN2fTrO9L3vKuOzt~0n8Bia~MWoNFU67cVZJt6WuEAmZAPskZZDX5iw__&Key-Pair-Id=K3RDDB1TZ8BHT8' width='270' height='280' style='border-radius:7px;'><br>",unsafe_allow_html=True)

country_code=st.text_input("Country Code",help="Enter country code",placeholder="+91",max_chars=4)

phone_num=st.text_input("Receiver Phone Number",help="Enter phone number",placeholder="9876543210",max_chars=10)

original_number=country_code+phone_num

hour=st.number_input("Set the Hour",help="Enter the hour in 24-hour format",format="%d",min_value=0,max_value=23)

minutes=st.number_input("Set the Minute",help="Specify the minutes (00-59)",format="%d",min_value=0,max_value=59)

message=st.text_area("Your Message",help="Type your message here")
 
total_seconds=None

btn=st.button("Send Message")

if btn:
        time=datetime.datetime.now().strftime("%H:%M:%S").split(":")
        curr_hours=int(time[0])
        curr_minutes=int(time[1])
        curr_seconds=int(time[2])

        def sendMessage():

            with st.spinner("Sending message..."):
            
                if(curr_hours>hour):
                    st.code("Your Message is scheduled to be sent on next day")

                elif(curr_hours<hour):
                    if(hour>0 and minutes>0):
                        total_seconds=((hour*3600)+minutes*60)-curr_seconds
                        st.code(f"Your message is scheduled to be sent in {total_seconds} seconds")
                    elif(hour>0):
                        total_seconds=(hour*3600)-curr_seconds
                        st.code(f"Your message is scheduled to be sent in {total_seconds} seconds")

                elif(curr_hours==hour):
                    if(minutes>curr_minutes):
                        total_seconds=((minutes-curr_minutes)*60)-curr_seconds
                        st.code(f"Your message is scheduled to be sent in {total_seconds} seconds")

                    else:
                        st.code("Your Message is scheduled to be sent on next day")

                pywhatkit.sendwhatmsg(original_number,message,hour,minutes,2)         
                st.success("Message Send Successfully!")

        if(len(phone_num)!=10):
                 st.error("Enter a valid Phone Number :(")
        elif "+" not in country_code:
                 st.error("Enter a valid Country Code :(")
        else:
             sendMessage()
        
# pywhatkit.playonyt("how to start coding in 1st year")

# +918439233368