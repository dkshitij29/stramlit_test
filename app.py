import streamlit as st

def main():
    # Personal Information
    st.title('Kshitij Dhannoda')
    st.write('Dearborn, MI')
    st.write('[Email](mailto:dkshitij@umich.edu) | [LinkedIn](https://www.linkedin.com/in/dkshitij29/) | GitHub: [Link](https://github.com/dkshitij29) ')

    # About Section
    st.header('About 🙋‍♂️')
    st.write("I am Kshitij Dhannoda, a passionate software engineer with a Master's in Computer and Information Sciences from the University of Michigan, Dearborn, and a Bachelor's in Information Technology from Vidya Jyothi Institute of Technology, India.")
    st.write("Skilled in JavaScript, Go, Rust, Java, Python, C, Dart, and PHP, I excel with frameworks like React-Native, Flutter, OpenCV, Hadoop, PySpark, Django, and Next.js. I also have expertise in tools such as GIT, Docker, and Android Studio.")
    st.write("My professional journey includes internships at the Free Software Movement of India and Provoke Developers, where I enhanced user experiences and developed interactive web applications. I possess strong soft skills in communication, collaboration, and leadership.")
    st.write("I have mentored aspiring technologists as an Internship Coordinator for Swecha and a Tech Lead for the GNU/Linux User Group, promoting open-source initiatives. Driven by a passion for continuous learning, I am eager to tackle new challenges and contribute to impactful projects.")

    # Education Section
    st.header('Education')
    st.subheader('University of Michigan, Dearborn, MI')
    st.write('Masters in Computer and Information Sciences (General)')
    st.write('Jan 2024 - Jan 2026')

    st.subheader('Vidya Jyothi Institute of Technology, India')
    st.write('Bachelor of Technology in Information Technology')
    st.write('Aug 2019 - May 2023')
    

    # Work Experience Section
    st.header('Work Experience')

    st.subheader('Next.js Developer - Internship | Provoke Developers, India')
    st.write('Oct 2022 – Nov 2022')
    st.write('''
    - Translated Figma designs to interactive webpages, enhancing the business’s online presence by 15%.
    - Consolidated designs into a unified app, utilizing Git for version control, facilitating business feature maintenance.
    - Utilized dynamic scaling to efficiently cover 95% of screen sizes, boosting the business’s online presence.
    - Implemented responsive design principles with Next.js, enhancing user experience for a 40% satisfaction boost.
    ''')

    st.subheader('Core Representative and Design Lead - Apprenticeship | GNU/Linux User\'s Group of VJIT, India')
    st.write('Oct 2020 – Nov 2023')
    st.write('''
    - Oversaw maintenance, design, and deployment of the VJIT GLUG Website built on WordPress.
    - Organized GLUG conference for a cohort of roughly 500–600 students, focusing on Open Source Software and Hardware.
    - Implemented responsive design principles, ensuring and enhancing user experience.
    ''')

    # Projects Section
    st.header('Projects')
    st.subheader('Graph Shortest Path Visualization')
    st.write('Learn more about the Graph Shortest Path Visualization project.')


    st.write('**Project Description**')
    st.write('''
    The Graph Shortest Path Visualization project aims to visualize graphs represented by adjacency matrices, compute the shortest path between two nodes using Breadth-First Search (BFS), and plot the nodes and shortest path on a grid. This project leverages Python programming along with libraries such as NetworkX and Matplotlib.
    ''')
    st.write('**Key Features**')
    st.write('''
    - **Graph Visualization**: The project enables the creation and visualization of graphs based on given adjacency matrices. It utilizes NetworkX and Matplotlib to generate graphical representations of the graphs.
    - **Shortest Path Calculation**: Using the Breadth-First Search (BFS) algorithm, the project computes the shortest path between two nodes within the graph. This functionality facilitates analyzing connectivity and optimal routing in graph-based systems.
    - **Interactive Plotting**: The system provides interactive plotting capabilities to visualize the nodes and shortest path on a grid. This feature enhances the understanding of graph structures and facilitates effective communication of insights.
    ''')
    st.write('**Tools and Technologies**:')
    st.write('Python, NetworkX, Matplotlib.')
    st.write('**Usage Scenario**')
    st.write('''
    The Graph Shortest Path Visualization project finds applications in various domains such as network analysis, transportation systems, and spatial data analysis. It can be utilized by researchers, engineers, and analysts to explore and analyze complex relationships within graph-based datasets, aiding in decision-making processes and optimization strategies.
    ''')
    st.write('**Significance and Novelty**')
    st.write('''
    This project showcases proficiency in graph theory, algorithmic problem-solving, and data visualization techniques. It demonstrates the ability to implement advanced algorithms and effectively communicate insights through visual representations. The project’s versatility makes it a valuable tool for addressing a wide range of real-world problems requiring graph analysis and visualization.
    ''')



    st.subheader('Step Tracker Application')
    st.write('Learn more about the Step Tracker Application project.')
    st.write('**Project Description**')
    st.write('''
    The standalone step tracking app, developed with Flutter, not only breaks free from the limitations of closed-source, platform-specific health tracking apps but also prioritizes user privacy as its central tenet. By leveraging the versatility of Flutter, the app runs seamlessly across various platforms, including Android, iOS, and custom ROMs, ensuring accessibility for all users. The decision to store all data locally on users’ devices, coupled with the utilization of device sensors for step counting, reflects a privacy-by-design approach that minimizes reliance on external servers and preserves user anonymity. With the use of a SQLite database to manage step counts and long-term progress, the app provides a secure environment for users to track their health data without compromising their privacy, empowering them with full control over their information.''')

    st.write('**Key Features**')
    st.write('''
    - Real-Time Step Counting: Utilize the accelerometer’s Z-axis readings to detect and count user steps in real-time.
    - Intuitive Display: Display the current step count prominently on the main screen, providing users with immediate feedback on their activity level.
    - Data Persistence: Implement SQLite to store daily step counts, ensuring that users can track their progress over time.
    - Historical Data Tracking: Allow users to view their step history, offering insights into their activity patterns and motivating consistent exercise.
    - User Notifications: Send notifications to users to encourage regular activity and remind them to meet their step goals.
    - Customizable Goals: Enable users to set daily step goals, promoting personalized fitness targets and enhancing motivation.
    - User-Friendly Interface: Design a clean and intuitive interface that makes it easy for users of all ages to navigate and use the app.
    ''')
    st.write('**Tools and Technologies**')

    st.write("Flutter, Dart, SQLite.")

    st.write('**Significance and Novelty**')

    st.write("The Step Tracker Application exemplifies proficiency in mobile app development using Flutter and Dart. By integrating sensor data and persistent storage, the app provides a practical tool for promoting physical activity and healthy living. The project demonstrates the ability to design user-centric mobile applications that leverage hardware sensors and databases to deliver meaningful health insights.")


    # Web Leave Management System Project
    st.subheader('Web Leave Management System')
    st.write('**Project Description**')
    st.write('''
    The Web Leave Management System is a comprehensive web-based application designed to streamline the leave request and approval process within the university environment. The system facilitates efficient management of leave applications, tracking of leave balances, and communication between faculty, staff, and administrators.
    ''')
    st.write('**Key Features**')
    st.write('''
    - **User-Friendly Interface**: The system features a user-friendly interface accessible to faculty, staff, and administrators, allowing them to submit, review, and approve leave requests with ease.
    - **Leave Tracking and Balances**: Employees can view their leave balances and history, enabling them to make informed decisions when planning leave and ensuring compliance with university policies.
    - **Automated Workflows**: The system automates the leave approval process, reducing administrative burden and ensuring timely processing of leave requests. Email notifications are sent to notify stakeholders of pending requests and approvals.
    - **Customizable Settings**: Administrators have the ability to customize settings such as leave types, accrual rates, and approval workflows to align with university policies and requirements.
    - **Reporting and Analytics**: The system provides reporting and analytics capabilities, allowing administrators to track leave trends, analyze usage patterns, and generate insights to inform decision-making.
    ''')
    st.write('**Technologies Used**')
    st.write('HTML, CSS, JavaScript, PHP, XAMP (web server).')

    # Recommendation System Project
    st.subheader('Recommendation System')
    st.write('**Project Repository**: [Git Repo Link](https://github.com/dkshitij29/recommendation_system)')  # Replace with your actual Git repo link
    st.write('**Overview**')
    st.write('Developed a recommendation system to suggest relevant items based on category and price range using pandas data frames for data manipulation.')
    st.write('**Key Responsibilities**')
    st.write('''
    - Designed and implemented a Python-based recommendation algorithm.
    - Created and maintained project files, including Project.ipynb for the core Python code and merged df.csv for the dataset.
    - Authored comprehensive documentation in README.md to guide users through setup and usage.
    ''')
    st.write('**Setup and Configuration**')
    st.write('''
    - Ensured compatibility with Python environments and facilitated setup through detailed instructions:
        - Instructed users to install dependencies via pip.
        - Provided a step-by-step guide for cloning the repository and launching the Jupyter notebook.
        - Enabled alternative usage via Google Colab for increased accessibility.
    ''')
    st.write('**Usage and Examples**')
    st.write('''
    - Configured the system to prompt users for category and price range inputs.
    - Generated relevant item recommendations based on user inputs.
    - Included a practical example for testing, focusing on “Gift Wrapping Supplies” within a specified price range.
    ''')
    st.write('**Data Management**')
    st.write('''
    - Ensured dataset integrity by requiring specific columns (title, category name, price, etc.) and proper formatting.
    - Utilized pandas data frames to streamline data manipulation and enhance performance.
    ''')
    st.write('**Future Improvements**')
    st.write('''
    - Proposed designing an add-on system to categorize items into parent categories for improved input accuracy.
    - Outlined plans for developing a data-independent system, building upon the current design to handle diverse datasets.
    ''')
    st.write('**Tools and Technologies**')
    st.write('Python, Pandas, Jupyter Notebook, Google Colab.')

    # Caliber Web Docker Image Customization Project
    st.subheader('Caliber Web Docker Image Customization')
    st.write('**Project Description**')
    st.write('The Caliber Web Docker Image Customization project involves the customization of the Caliber Web application using Docker containers to meet specific use cases within the university environment. This project leverages Docker technology to create a scalable and portable solution for managing academic assessment processes.')
    st.write('**Key Features**')
    st.write('- **Caliber Web Integration:** Integrates the Caliber Web application within the university’s academic infrastructure for efficient management of assessment tasks, grading, and feedback processes.')
    st.write('- **Customization for University Use Cases:** Tailors the Caliber Web Docker image to align with unique requirements such as course management, student enrollment, faculty collaboration, and administrative oversight.')
    st.write('- **Scalability and Portability:** Ensures scalability and portability across different computing environments by containerizing the application using Docker, facilitating seamless deployment and management.')
    st.write('**Tools and Technologies**')
    st.write('Docker, Caliber Web, Linux, Shell Scripting')
    st.write('**Usage Scenario**')
    st.write('The Caliber Web Docker Image Customization project serves as a centralized platform for academic assessment and evaluation within the university. It provides a user-friendly interface for creating, managing, and analyzing assessment data, enhancing communication and collaboration among stakeholders.')
    st.write('**Significance**')
    st.write('This project demonstrates proficiency in DevOps practices, containerization techniques, and software customization. It showcases the ability to adapt and tailor applications to meet specific organizational needs, improving efficiency within academic institutions and enhancing teaching and learning experiences through enhanced assessment management.')


    # Speech2text and Text2speech mobile app
    st.subheader('Speech2text and Text2speech Mobile App')
    st.write('**Project Description**')
    st.write('The project involves developing a speech recognition API using Flutter for Android devices. It captures speech or acoustic signals, transforms them into text using the speech_to_text package version 6.6.2, and displays the translated text on the Android device.')
    st.write('**Preparations**')
    st.write('- Collected speech/acoustic signals.')
    st.write('- Transformed speech to text using the speech_to_text package version 6.6.2.')
    st.write('- Displayed the translated text on the Android device.')
    st.write('**Output**')
    st.write('- Added all necessary permissions in AndroidManifest.xml.')
    st.write('- Designed the UI of the app in the main activity XML.')
    st.write('- Edited MainActivity.java:')
    st.write('  - Initialized variables and functions such as TextViews, SpeechRecognizer object, MediaPlayer, and Recorder objects.')
    st.write('  - In the onCreate function, built the RecView layout, created the SpeechRecognizerIntent, and set onclick listeners.')
    st.write('  - Used putExtra() in SpeechRecognizerIntent to store data and add extra data into the intent object.')
    st.write('  - Created startRecording to begin voice recording and handle permissions.')
    st.write('  - Implemented OnActivityResult to retrieve transcribed results and display them in TextView.')
    st.write('  - Edited MediaPlayer object to playback audio from the recorded file and handle playback control.')
    st.write('**Challenges**')
    st.write('- Dealing with two mic inputs simultaneously.')
    st.write('- Transcribing directly from an audio file required format conversion and consideration of costs for using Google Cloud API.')
    st.write('- Implemented speech recognition on audio replay to transcribe replayed audio.')
    st.write('**Tools and Technologies**')
    st.write('Flutter, Dart, speech_to_text: ^6.6.2')
    st.write('**Final Report**')
    st.write('Presentation Deadline: 4/15/2024. Show all files, important classes, and functions.')
    st.write('Submission Deadline: 4/19/2024. Include source code, slides, experimental results (audio and text files), and a recorded video for specific demos.')
    st.write('[Back to Portfolio](#)')


    # Contact Section
    st.header('Contact Me')
    contact_form = st.form(key='contact_form')
    name = contact_form.text_input(label='Enter your name')
    email = contact_form.text_input(label='Enter your email')
    message = contact_form.text_area(label='Your message')
    submit_button = contact_form.form_submit_button(label='Submit')

    if submit_button:
        st.write(f'Thank you {name}! Your message has been received.')


# Run the app
if __name__ == '__main__':
    main()
