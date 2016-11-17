# PROJECT DAYDREAM
# Technical Review 1

## Synthesis

### Issues raised
- Indico vs OpenCV (resolved)
 - We will be doing primary experimentation in OpenCV. Reasons for this choice include:
   - Less latency 
   - Does not require networking
   - Trainability (open to learning and refinement)
 - Drawbacks:
   - Hard to train specifically


- False positives / frame handling
-- Implement a two-second delay so that an animation does not trigger prematurely
--- Once the delay passes successfully, the animation sequence becomes uninterruptible - cutting out mid-way will not be possible.


- Teaming 
-- Feature development should be pre-agreed upon
-- Decide on features for each subteam to work on in parallel 
-- Open communication and making sure that everyone is receiving notifications from the Slack channel
-- Trello/project management platform 


## Post-review discoveries


- Other APIs
Other compatible APIs were found as a result of our continuing process to search for a suitable platform - one such platform is the YOLO Project (link below)
http://pjreddie.com/darknet/yolo/ 


- Multi-tasking
Class instantiation is required to detect multiple objects and initialize parallel counters for their animation processes
System diagram should be updated to reflect the multi-object recognition capability required of the project
Demo was able to detect multiple objects (in OpenCV)


## Process reflection

- Overall, we were able to communicate the intents and objectives of the project to the audience.
- We were also really proud that we had functionality prior to the technical review and were able to live-demo.
- We got feedback for our key questions, but they were not necessarily as in-depth as we would have liked.
One potential cause for this problem is that our questions were not open-ended enough
I.e. OpenCV vs. Indico?
The lack of depth in our questions contributed to the limited responses we received
- Notably, our system diagram did not account for multi-tasking functionality - something which we realized after the discussion process.
Although it can be fixed (discussed more above), we feel that this was a glaring error branching from our lack of attention to detail in our technical review.


- Next time:
We will organize this more cohesively by using slide decks
We will practice more specifically what we are going to say and who’s going to say it.
We will continue to use demos whenever possible, to illustrate our progress and ideation translation
However, we will try to ask more discussion-spurring questions about our demos.

