import express, { Router } from 'express';
import { faqController } from '../../modules/faq';

const router: Router = express.Router();

router
  .route('/')
  .post(faqController.createFaq)
  .get(faqController.getFaqs);

export default router;