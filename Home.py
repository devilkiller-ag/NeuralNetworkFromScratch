import streamlit as st

st.title("Neural Network Concepts Implemented from Scratch!")
st.write(
    "This is a simple web app that demonstrates the concepts of neural networks implemented from scratch."
)

# ################################### About the author #########################################
st.subheader("About the author: [Ashmit JaiSarita Gupta](https://ashmit.dev/)")

st.write(
    """
    I am an engineering physics undergraduate passionate about Quantum Computing, Machine Learning, UI/UX, and Web Development. I am a student driven by the community and who shares what he has learned. I love to work on real world projects about the topics I learn which can be used by others. To accomplish this I frequently attend hackathons and collaborate with companies to work on real-world projects related to my domains. Feel free to contact me if your company is interested in working on awesome projects in these fields with me. I’m currently building most frequently with: JavaScript/Typescript, C++, and Python. Some of the main frameworks and libraries I frequently use are: React.js,Express.js, Tailwind CSS, ShadCN UI, Qiskit,and Pytorch. Explore the below links to explore more about me, my previous projects, blogs, and experience at various organizations.
"""
)

# ############ Socials ############
c1, c2, c3 = st.columns(3)
with c1:
    st.info(
        "**Portfolio: [Ashmit JaiSarita Gupta](https://ashmit.dev/)**",
        icon="🔥",
    )
with c2:
    st.info(
        "**GitHub: [@devilkiller-ag](https://github.com/devilkiller-ag)**", icon="😸"
    )
with c3:
    st.info(
        "**GitLab: [@devilkiller-ag](https://gitlab.com/devilkiller-ag)**", icon="🚀"
    )


c4, c5, c6 = st.columns(3)
with c4:
    st.info(
        "**LinkedIn: [ashmit-jaisarita-gupta](https://www.linkedin.com/in/ashmit-jaisarita-gupta/)**",
        icon="🌐",
    )
with c5:
    st.info("**Twitter: [@jaisarita](https://github.com/devilkiller-ag)**", icon="🐤")
with c6:
    st.info("**Hashnode: [jaisarita](https://jaisarita.hashnode.dev/)**", icon="✍🏻")
