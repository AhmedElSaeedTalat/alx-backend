import { createQueue } from 'kue';
/* module to create a queue */

/* create the queue */
const queue = createQueue();
const data = {
	phoneNumber: 1068892003,
	message: 'notification data',
}


/* create job and save it to the queue */
const job = queue.create('push_notification_code', data);
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

/* listen to the job when completed  */
job.on('complete', () => {
  console.log('Notification job completed');
});

/* listen to the job when failed */
job.on('failed', () => {
  console.log('Notification job failed');
});
