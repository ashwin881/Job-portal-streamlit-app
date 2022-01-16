import streamlit as st 
import streamlit.components.v1 as stc
import requests 
from bs4 import BeautifulSoup

base_url = 'https://www.linkedin.com/jobs/search?keywords={}&location={}&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
JOB_HTML_TEMPLATE = """


<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div class="container d-flex flex-wrap">
    <div class="card text-dark bg-info mb-3" style="max-width: 18rem; width:100% ;height: 100%">
  <div class="card-header">{}</div>
  <div class="card-body">
    <h5 class="card-title">{}</h5>
    <p class="card-text">apply on Linkedin</p>
  </div>
</div>
</div>
  
"""

def main():
    menu=['Home','About']
    choice = st.sidebar.selectbox('Menu',menu)
    st.title("Job FindR Portal")
    if choice == 'Home':
        
        st.subheader('Home')
        
        with st.form(key="searchform"):
            nav1,nav2,nav3=st.columns([3,2,1])
            with nav1:
                search_term=st.text_input("Search job")
            with nav2:
                location=st.text_input("Location")
            with nav3:
                st.text("Search")
                submit=st.form_submit_button(label='Search')
        
        col1,col2=st.columns([2,1])
        with col1:
            if submit:
                st.success("you searched for {} in {}".format(search_term,location))
                search_url=base_url.format(search_term,location)
                page=requests.get(search_url).text
                soup=BeautifulSoup(page,"lxml")
                role = [p.text.strip() for p in soup.find_all(class_="base-search-card__title")]
                cname= [p.text.strip() for p in soup.find_all(class_="base-search-card__subtitle")]
                res=dict(zip(role,cname))
                no_res=len(res)
                st.subheader("Showing {} jobs.".format(no_res))
                for key,value in res.items():
                    st.markdown(JOB_HTML_TEMPLATE.format(key,value),unsafe_allow_html=True)
        with col2:
            with st.form(key='email_form'):
                st.write("To get more job info share ur email")
                email=st.text_input('Email')
                submit_email=st.form_submit_button(label='Subscribe')
                if submit_email:
                    st.success("message sent to {}".format(email))
    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
                
                    
                
                