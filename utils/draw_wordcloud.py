from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = """
1. Synchronous Pacing
Everyone is expected to move at roughly the same pace.

Lessons, activities, and assignments are structured around a fixed schedule.

There’s often little flexibility to skip ahead or slow down.

2. Teacher-Centered Delivery
A teacher or facilitator is seen as the primary source of knowledge.

Most content is delivered through lectures or demonstrations.

Learners are expected to listen, take notes, and ask questions at designated times.

3. Pre-Defined Curriculum
The course has a set syllabus with specific topics and outcomes.

The learning path is usually linear—Topic A leads to Topic B, and so on.

Learners have limited input into what or how they learn.

4. Passive Learning
A lot of time is spent consuming information (e.g. watching slides, listening to explanations).

Activities are often focused on remembering and repeating information (e.g. quizzes, fill-in-the-blank exercises).

Active problem-solving or application of knowledge may be limited or delayed until later in the course.

5. Assessment-Driven
Progress is measured through formal assessments (e.g. tests, exams, or graded projects).

Feedback is often summative ("you got 7/10") rather than formative ("here’s how to improve").

Learners may feel pressure to perform rather than experiment or take risks.

6. One-Size-Fits-All Design
Little differentiation between learners with different backgrounds, learning styles, or needs.

Success often depends on adapting to the instructor’s style rather than the other way around.

Students who fall behind may struggle to catch up; those who move faster may feel bored.
"""

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

wordcloud.to_file("wordcloud.png")

# Display the generated image
# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")  # No axes
# plt.title("Word Cloud Example", fontsize=16)
# plt.show()
