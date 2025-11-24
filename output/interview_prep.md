# Interview Prep: Mangomint – Senior Fullstack Engineer

## 1. Job Overview

| Attribute | Detail |
| :--- | :--- |
| **Role** | Senior Fullstack Engineer (Technical Lead for SalonJobs) |
| **Company** | Mangomint (SaaS for the Beauty/Wellness Industry) |
| **Project Focus** | **SalonJobs**: An experimental, ambitious greenfield product aiming to be the industry's default hiring solution. |
| **Key Deliverable** | Rapidly iterate, own major technical decisions (architecture, stack, infrastructure), and drive the product from concept to proven market fit. |
| **Required Stack** | **Next.js (preferred)**, **TypeScript**, Node, **Drizzle ORM**, PostgreSQL, Vercel, Docker. |
| **Compensation** | \$160,000 - \$180,000 + Equity/Stock Options |

## 2. Why This Job Is a Fit

This role is a high-alignment opportunity requiring a unique blend of deep technical skill and an entrepreneurial mindset, which aligns perfectly with your documented senior experience.

*   **Architectural Ownership:** The requirement to "Own major technical decisions across the stack" aligns directly with your experience leading the migration and defining the architecture at ScaleUp SaaS Solutions.
*   **Tech Stack Mastery:** Your specific expertise in **Next.js, TypeScript, Node.js, and Drizzle ORM** is precisely what Mangomint is using for this new, high-velocity product line, minimizing ramp-up time and maximizing immediate contribution.
*   **Startup Velocity:** The focus on "fast iteration," "experimentation," and operating in short cycles directly maps to your successful track record of taking features "from idea to production quickly" in growth environments.
*   **Product Focus:** Your demonstrated ability to partner closely with Design and translate **Figma** concepts into polished products satisfies the "strong product sense" requirement critical for Mangomint’s design-led approach.

## 3. Resume Highlights for This Role

Focus heavily on demonstrating measurable results and senior-level decision-making tied to the specific required technologies.

| Job Requirement Focus | Your Resume Proof Points |
| :--- | :--- |
| **Architectural Ownership** | "Owned major technical decisions for the core application, migrating the stack to **Next.js 14** and **TypeScript** (full-stack), resulting in 99.9% uptime..." |
| **Fast Iteration & Delivery** | "Operated with an entrepreneurial mindset, taking ownership of ambiguous features from initial concept (idea stage) to production deployment on **Vercel** within two-week sprints." |
| **Specific Stack Mastery** | "Designed and implemented a robust **PostgreSQL** schema, utilizing **Drizzle ORM** for type-safe data access, enhancing developer velocity..." |
| **Product Sense / Design** | "Partnered directly with Product and Design teams, translating high-fidelity **Figma** prototypes into responsive, accessible, and polished user interfaces." |
| **Infrastructure/DevOps** | "Managed containerized development environments using **Docker** and collaborated with DevOps to integrate automated testing (**Playwright**) and monitoring (**Sentry**)." |

## 4. Company Summary

Mangomint provides modern, high-quality, cloud-based management software for the beauty and wellness industry (salons, spas). They differentiate themselves through a focus on intuitive design and robust technology, contrasting with outdated incumbents.

*   **Core Business:** SaaS providing Booking, POS, Client Management, and Inventory tools.
*   **Strategic Direction (SalonJobs):** This role is centered on a high-stakes, **greenfield expansion** into the talent acquisition space. This means the company is leveraging its existing market share to solve a major industry problem (hiring), making this a highly visible, strategic product line.
*   **Culture:** Fast-paced, design-focused, and committed to modern, efficient technology stacks. They are looking for self-starters who thrive in ambiguity (essential for finding PMF).

## 5. Predicted Interview Questions

Prepare detailed, STAR-formatted answers for the following categories, ensuring you use the required technologies (Next.js, Drizzle, TypeScript) in your technical examples.

### A. Behavioral & Leadership (Entrepreneurial Mindset)

1.  **The Ambiguity Challenge:** "The SalonJobs initiative requires working in short, focused cycles that prioritize learning and experimentation. Describe a time you had to pivot a major feature or abandon a significant technical investment due to new product learnings or a lack of PMF. How did you handle the execution and communication?"
    *   *Strategy:* Emphasize comfort with change, focusing on maximizing **impact** and minimizing waste of effort.
2.  **Architectural Decision Ownership:** "Tell me about the most significant architectural decision you owned in your previous role. What were the alternatives, how did you justify your choice to stakeholders, and what was the quantifiable long-term outcome (performance, dev velocity, stability)?"
    *   *Strategy:* Use an example related to the shift to Next.js or a complex database schema change using Drizzle/PostgreSQL.
3.  **Cross-Functional Partnership (Figma to Code):** "The role requires close partnership with Design. Walk me through a challenging experience where translating a complex Figma concept into a production feature was difficult. How did you collaborate with the designer to ensure technical feasibility while maintaining UI quality?"

### B. Technical Deep Dive (Stack Specific)

4.  **Next.js Architecture:** "When building a high-traffic application with Next.js, how do you strategically distribute logic between **Server Components and Client Components** to optimize initial load time and maintain interactivity? Give a specific example of when you would rely heavily on Server Actions/Components."
5.  **Type Safety and ORMs:** "Mangomint uses Drizzle ORM. What advantages does a highly type-safe ORM like Drizzle (compared to, say, raw SQL or Prisma) offer in a fast-iteration environment? Describe a complex query or transactional logic you implemented using a similar modern ORM."
6.  **Scalability and Infra (Vercel):** "Since you will be working with Vercel/Supabase infrastructure, describe your approach to ensuring a Next.js application remains scalable and cost-effective under sudden traffic spikes. How do you monitor and optimize backend/database performance?"
7.  **System Design:** "Design the core data schema and API endpoints for the initial MVP of SalonJobs (e.g., job postings, candidate profiles, application tracking). Focus on the relationship between PostgreSQL tables and how you'd query them efficiently."

## 6. Questions to Ask Them

Use these questions to show genuine interest in the SalonJobs strategy and your fit as a technical owner.

### Focused on Strategy and PMF (Greenfield Project)

1.  "Given that SalonJobs is an experimental venture, what is the current **go-to-market strategy**? Are we prioritizing the employer (salons) side or the candidate (job seeker) side first, and how does the technical roadmap reflect that?"
2.  "Can you describe the initial MVP state of SalonJobs? What is the single biggest technical risk or unknown you are currently facing, and how are you planning to mitigate it?"
3.  "How is the technical debt or 'experimentation code' managed? If a feature proves successful, what process ensures it is refactored into a scalable, long-term architectural solution?"

### Focused on Engineering and Ownership

4.  "Since I will be owning major architectural decisions, how often does the SalonJobs team sync with the broader Mangomint engineering leadership to ensure alignment on security standards, deployment protocols, and core utility patterns?"
5.  "Could you elaborate on the use of **Supabase** in the current infrastructure? Is it primarily used for its database features, or are the Auth/Edge functions being utilized for the SalonJobs project?"

## 7. Concepts To Know/Review

A quick review of these concepts will ensure you can speak confidently about the modern stack.

| Concept | Review Focus |
| :--- | :--- |
| **Next.js 14+** | Deep understanding of the App Router, Server Components, Server Actions, and data caching strategies (`fetch()` options, Vercel/CDN caching). |
| **Drizzle ORM** | Type-safe schema definition, relational queries (joins), transactions, and migrations strategy. Be prepared to compare it favorably to Prisma or Knex. |
| **Vercel Deployment** | Serverless functions (lambdas), Edge functions, environment variables, monorepo support, and monitoring using Vercel Analytics/Observability. |
| **TypeScript Utility** | Advanced types, Zod or similar schema validation (often paired with Drizzle), and why full-stack type safety is crucial for development speed. |
| **Agile & Iteration** | Be ready to discuss how you manage technical quality in two-week (or shorter) cycles, including defining a "definition of done" that includes testing (Playwright) and monitoring (Sentry). |

## 8. Strategic Advice

### Tone and Persona

*   **Be the Owner:** Throughout the interview, adopt the mentality of a technical lead. Don't just describe what you built; describe *why* you chose to build it that way. Use words like "architected," "owned," "defined," and "led."
*   **Emphasize Product Sense:** Whenever discussing technical work, tie it back to the business or user outcome. Example: "We chose Next.js Server Components *to reduce Time To Interactive*, which directly increased our conversion rate on mobile."
*   **Embrace Ambiguity:** Mangomint is hiring for a greenfield, experimental project. Show excitement for the unknown and the challenge of finding PMF. If asked about uncertainty, respond with your structured process for learning and iteration.

### Key Areas to Emphasize

1.  **Architecture vs. Execution:** You must prove you can both *design* the system (senior role) and *deliver* the code (hands-on contributor). Ensure your examples balance strategic vision with tactical implementation details.
2.  **Ecosystem Expertise:** Do not just say you know React; focus on **Next.js**'s specific advanced features (App Router, Server Components) and how you leverage **Vercel** for optimal deployment.
3.  **Data Layer Proficiency:** Since they use Drizzle/PostgreSQL, treat the data layer as a critical architectural component. Discuss performance optimization for complex job search queries (potentially mentioning Algolia, which is in their stack).

### Red Flags to Avoid

*   **Avoiding Trade-offs:** Do not present a technical decision as universally perfect. Senior engineers discuss the trade-offs (e.g., "While X provided high performance, the initial configuration cost was higher...")
*   **Focusing on Maintenance Only:** Avoid examples centered on bug fixing or maintaining legacy code. Focus all stories on *building*, *scaling*, or *migrating* high-impact features.
*   **Lack of Product Context:** Do not let technical conversations drift away from the user or business impact. Remember that SalonJobs' success is measured by its market penetration, not just clean code.