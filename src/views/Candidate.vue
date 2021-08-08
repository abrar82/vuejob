<template>
<div>
   <button @click.prevent="created" :disabled="isLoading">Show</button>
    <div v-if="!isLoading">
        <ul id="example-2" v-if="!isApplyJob">
        <li v-for="job in data" v-bind:key="job.id">
           <h3 >Job Name : {{job.job_name}}</h3>
	<h3>Job Description : {{job.description}}</h3>
	<h3>Job Qualification :{{job.qualification}}</h3>
	<h3>Job Location :{{job.job_location}}</h3>
	<h3>Salary : {{job.salary}}</h3>
    
	 <button v-on:click="applyJob(job)" >Apply job</button>
	<!-- <button on:click={ applyJob(job) }   hidden = {candihide}>
		Apply Job
	</button> -->
	<!-- <button on:click={ deleteJob(job) } hidden = {adminhide} disabled= {candisabled} >
		Delete Job -->
	<!-- </button> -->
	<hr>
        </li>
        </ul>
        <div v-else-if="isFormVis">
            <h5>You are applying for</h5>
            <h4>Job Name : {{jobData.job_name}}</h4>
            <h4>Job Description : {{jobData.description}}</h4>
            <h4>Job Location : {{jobData.job_location}}</h4>
            <label class="input-label" for="applicantName">
	Applicant Name : 
	<input
	class="wide"
	id="applicantName"
	name="applicantName"
	v-model="application.applicant_name"
	type="text"
	data-multistep-error-message="name couldn't be empty"
	placeholder="Enter Applicant Name" 
   />
</label><br><br>
<label class="input-label" for="applicantPhone">
	Applicant Phone : 
	<input
	class="wide"
	id="applicantPhone"
	name="applicantPhone"
	v-model="application.applicant_phone"
	type="text"
	data-multistep-error-message="name couldn't be empty"
	placeholder="Enter Applicant Phone Number" 
   />
</label><br><br>
<label class="input-label" for="applicantEmail">
	Applicant Email : 
	<input
	class="wide"
	id="applicantEmail"
	name="applicantEmail"
	v-model="application.applicant_email"
	type="text"
	data-multistep-error-message="name couldn't be empty"
	placeholder="Enter Applicant Email" 
   />
</label><br><br>

	 <button v-on:click="submitApplication(application)" >Submit Application</button>
      <button v-on:click="resetData" >Reset Application</button>
        </div>
        <div v-else>

        </div>
    </div>
 </div>
</template>

<script>// @ts-nocheck

// var example2 = new Vue({
//   el: '#example-2',
//   data: {
//     parentMessage: 'Parent',
//     items: [
//       { id: 1, message: 'Foo' },
//       {  id: 2,message: 'Bar' }
//     ]
//   }
// })
export default {
    data(){
        return{
               jobData:{
                job_id:"",
                job_name:"",
                description:"",
                role : '',
                experience : '',
                qualification: '',
                job_location : '',
                salary: ''
            },
             application: {
                application_id : "",
                job_id : "",
                job_name :"",
                applicant_id :  "candidate@screel.in",
                applicant_name : "",
                applicant_phone : "",
                applicant_email : "",
                applied_time : ""
            },
         
             parentMessage: 'Parent',
            isLoading:false,
            isFormVis:false,
            isApplyJob:true,
            data :[],
        }
    },
methods:{
    resetData:function(){
        // this.application.application_id ="",
        // this.application.job_id = "",
        // this.application.job_name ="",
        // this.application.applicant_id =  "",
        this.application.applicant_name = "",
        this.application.applicant_phone = "",
        this.application.applicant_email = "",
        this.application.applied_time =""

        // this.jobData.job_id="",
		// this.jobData.job_name="",
		// this.jobData.description="",
		// this.jobData.role = '',
		// this.jobData.experience = '',
		// this.jobData.qualification= '',
		// this.jobData.job_location = '',
		// this.jobData.salary= ''
    },
    async created() {
        this.isLoading = true
  // GET request using fetch with async/await
  const response = await fetch("http://127.0.0.1:8000/jobs");
  this.data = await response.json();
  console.log(this.data)
        this.isApplyJob = false
        this.isLoading = false
//   this.totalVuePackages = data.total;
},
applyJob:function(job){
    this.isApplyJob = true
    this.jobData = job
    this.application.application_id=Math.floor(Math.random() * Date.now()),
              this.application.job_id = job.job_id,
              this.application.job_name =job.job_name,
    this.application.applied_time = Date.now()
     this.isFormVis = true
// console.log(this.application)
},
async submitApplication(){
    
if (confirm('Are you sure to Apply for '+  this.jobData.job_name +' Job?')) {
 const requestOptions = {
    method: "POST",
    headers: { 'accept': 'application/json',
    			'Content-Type': 'application/json' },
    body: JSON.stringify(this.application)
  };
  const response = await fetch("http://127.0.0.1:8000/jobs/apply", requestOptions);
  const data = await response.json();
  	if (response.ok) {
alert("Job Applied Successfully!!")
console.log(this.application)
console.log(data)
      }else{
console.log("Failed")
      }
  
}

}
}
}
</script>

<style>

</style>