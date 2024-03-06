import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { expect } from 'chai';



const queue = createQueue();
const list = [{phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'}];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });
  it('test the creation of jobs', () => {
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.be.equal(1);
    expect(queue.testMode.jobs[0].type).to.be.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal({phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account'});
  });
});
