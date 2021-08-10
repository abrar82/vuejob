<template>
  <div>
   <button @click.prevent="displayJob" >Show Job</button>
   <button @click.prevent="displayCreateJob" >Create Job</button>
   <button @click.prevent="loadApplication">Applications</button>
    <div v-if="!isLoading">
        <ul id="example-2" v-if="!isApplyJob">
        <li v-for="job in data" v-bind:key="job.id">
           <h3 >Job Name : {{job.job_name}}</h3>
	<h3>Job Description : {{job.description}}</h3>
	<h3>Job Qualification :{{job.qualification}}</h3>
	<h3>Job Location :{{job.job_location}}</h3>
	<h3>Salary : {{job.salary}}</h3>
    
	 <button v-on:click="editJobView(job)" >Edit job</button>
	 <button v-on:click="deleteJob(job)" >Delete job</button>
	<!-- <button on:click={ applyJob(job) }   hidden = {candihide}>
		Apply Job
	</button> -->
	<!-- <button on:click={ deleteJob(job) } hidden = {adminhide} disabled= {candisabled} >
		Delete Job -->
	<!-- </button> -->
	<hr>
        </li>
        </ul>
         </div>
<br><br>
         <div v-if="isFormVis">
<div>
			<label class="input-label" for="jobId">
				Job Id : 
				<input
				class="wide"
				id="jobId"
				name="jobId"
				v-model="job.job_id"
				type="text"
				:disabled= editDisabled
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Name" 
			   />
			   
			</label><br><br>
			<label class="input-label" for="JobName">
				Job Name : 
				<input
				class="wide"
				id="JobName"
				name="JobName"
				v-model="job.job_name"
				type="text"
				:disabled= editDisabled
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Name" 
			   />
			   
			</label><br><br>
			<label class="input-label" for="description">
				Job Description : 
				<input
				class="wide"
				id="description"
				name="description"
				v-model="job.description"
				type="text"
				:disabled=editDisabled
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Description" 
			   />
			   
			</label><br><br>
			<label class="input-label" for="role">
				Job Role : 
				<input
				class="wide"
				id="role"
				name="role"
				v-model="job.role"
				type="text"
				:disabled=editDisabled
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter Job's Role" 
			   />
			   
			</label><br><br>
			<label class="input-label" for="experience">
				Job Experience : 
				<input
				class="wide"
				id="experience"
				name="experience"
				v-model="job.experience"
				type="text"
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Experience" 
			   />
			   
			</label><br><br>
			<label class="input-label" for="qualification">
				Job Qualification : 
				<input
				class="wide"
				id="qualification"
				name="qualification"
				v-model="job.qualification"
				type="text"
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Qualification" 
			   />
			   
			</label><br><br>
			<label class="input-label" for="location">
				Job Location : 
				<input
				class="wide"
				id="location"
				name="location"
				v-model="job.job_location"
				type="text"
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Location" 
			   />
			   
			</label><br><br>
			<label class="input-label" for="salary">
				Salary : 
				<input
				class="wide"
				id="salary"
				name="salary"
				v-model="job.salary"
				type="text"
				data-multistep-error-message="name couldn't be empty"
				placeholder="Enter job's Salary" 
			   />
			   
			</label><br><br>
            
            <button @click.prevent="submitJob" :disabled="!updateDisabled"  >Post Job</button>
            <button @click.prevent="updateJob" :disabled="updateDisabled" >Update Job</button>
			<!-- <button id="showBtn" name="showBtn" on:click={ doPost } hidden = {edithide} >
				post Job
			</button>
			<button id="editBtn" name="editBtn" {disabled}  on:click={ updateJob  } hidden = {createhide}   >
				Update Job
			</button> -->
		 </div>
         </div>
         <div v-if="isAppliVis">
             <ul id="example-2">
        <li v-for="application in applications" v-bind:key="application.id">
            <h3>Applicant Name : {{application.applicant_name}}</h3>
			<h3>Applicant Phone : {{application.applicant_phone}}</h3>
			<h3>Applicant Email : {{application.applicant_email}}</h3>
			<h3>Job Id : {{application.job_id}}</h3>
			<h3>Job Name : {{application.job_name}}</h3>
    
	 <!-- <button v-on:click="applyJob(job)" >Apply job</button> -->
	<!-- <button on:click={ applyJob(job) }   hidden = {candihide}>
		Apply Job
	</button> -->
	<!-- <button on:click={ deleteJob(job) } hidden = {adminhide} disabled= {candisabled} >
		Delete Job -->
	<!-- </button> -->
	<hr>
        </li>
        </ul>
         </div>
    </div>
</template>

<script>
export default {
data(){
    return{
        job:{
                job_id:"",
                job_name:"",
                description:"",
                role : '',
                experience : '',
                qualification: '',
                job_location : '',
                salary: ''
            },
            isLoading:false,
            isFormVis:false,
            isAppliVis:false,
            isApplyJob:false,
			editDisabled : false,
            updateDisabled:false,
            tempId:"",
            data :[],
            applications:[],
    }
},
methods:{
    async deleteJob(job){
	if (confirm('Are  you sure to Delete '+ job.job_name +' Job?')) {
			const res = await fetch(`http://127.0.0.1:8000/jobs?sl_id=${job.id}`, {
			method: 'DELETE',
			headers: {
				'accept': 'application/json',
			  }
		})
		
		if (res.ok) {
            alert("Job Deleted Successfully!!")
            this.displayJob()
			console.log(res)
  		return res.json();
		} else {
			console.log("Failed")
		}
		}
    },
    async updateJob(){
        if(this.job.experience && this.job.qualification && this.job.job_location && this.job.salary){

        
        if (confirm('Are  you sure to Update this '+ this.job.job_name +' Job?')) {		
		let editjobs={
			experience : this.job.experience,
			qualification: this.job.qualification,
			job_location : this.job.job_location,
			salary: this.job.salary
		}
		console.log(JSON.stringify(this.job))
		const res = await fetch(`http://127.0.0.1:8000/jobs?sl_id=${this.tempId}`, {
			method: 'PUT',
			headers: {
				'accept': 'application/json',
    			'Content-Type': 'application/json'
			  },
			body: JSON.stringify(editjobs)
		})
		
		if (res.ok) {
            alert("Job Updated Successfully!!")
			// resetData()
			console.log(res)
  		return res.json();
		} else {
			console.log("Failed")
			// throw new Error(users);
		}
	}
    }else{
        alert("Please fill all the Details")
    }
    },
    async submitJob(){

		if (confirm('Are  you sure to Create this '+ this.job.job_name +' Job?')) {		

		
		console.log(JSON.stringify(this.job))
		const res = await fetch(`http://127.0.0.1:8000/jobs`, {
			method: 'POST',
			headers: {
				'accept': 'application/json',
    			'Content-Type': 'application/json'
			  },
			body: JSON.stringify(this.job)
		})
		
		if (res.ok) {
			
            alert("Job Created Successfully!!")
			// resetData()
			 this.job.job_id="",
		this.job.job_name="",
		this.job.description="",
		this.job.role = '',
		this.job.experience = '',
		this.job.qualification= '',
		this.job.job_location = '',
		this.job.salary= ''
			console.log(res)
  		return res.json();
		} else {
			console.log("Failed")
		}
	}
    },
    editJobView(job){

 this.isLoading = false
        this.isAppliVis = false
        this.isApplyJob = true
        this.isFormVis = true
        this.updateDisabled = false
        this.editDisabled = true
        this.tempId = job.id
        this.job.job_id=job.job_id,
		this.job.job_name=job.job_name,
		this.job.description = job.description,
		this.job.role =job.role 
        
		this.job.experience = '',
		this.job.qualification= '',
		this.job.job_location = '',
		this.job.salary= ''

    },
    displayCreateJob(){
        this.isLoading = false
        this.isAppliVis = false
        this.isApplyJob = true
        this.isFormVis = true
        this.updateDisabled = true
        this.editDisabled = false

         this.job.job_id="",
		this.job.job_name="",
		this.job.description="",
		this.job.role = '',
		this.job.experience = '',
		this.job.qualification= '',
		this.job.job_location = '',
		this.job.salary= ''
    },
    displayApplication(){
        this.isLoading = true

    },
    async displayJob() {
        this.isAppliVis = false
        this.isFormVis = false
        this.isLoading = true
  // GET request using fetch with async/await
  const response = await fetch("http://127.0.0.1:8000/jobs");
  this.data = await response.json();
  console.log(this.data)
        this.isApplyJob = false
        this.isLoading = false
//   this.totalVuePackages = data.total;
},
async loadApplication() {
        
        // this.isFormVis = false
        // this.isLoading = true
  // GET request using fetch with async/await
  const response = await fetch("http://127.0.0.1:8000/jobs/applications?skip=0&limit=100");
  this.applications = await response.json();
  console.log(this.applications)
        this.isAppliVis = true
        this.isFormVis = false
        this.isLoading = false
        this.isApplyJob = true
        // this.isLoading = false
//   this.totalVuePackages = data.total;
},
}
}
</script>

<style>

</style>